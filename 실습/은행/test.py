import pymysql
import datetime
import pandas as pd


create = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액) VALUES (%s,%s,%s,%s,%s,%s)"
create_sa = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액, 만기해지일) VALUES (%s,%s,%s,%s,%s,%s,%s)"
in_out_create = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 잔액) VALUES (%s,%s,%s,%s)"
saving_create = "INSERT INTO 적금통장 (계좌번호, 예금주, 입금액, 잔액, 만기일) VALUES (%s,%s,%s,%s,%s)"
#in_deposit = 
#out_deposit = "INSERT INTO 입출금통장 (account, name, withdraw, balance) VALUES (%s,%s,%s,%s,%s)"


def getCon():
    conn = pymysql.connect(host= 'localhost', port=3306, user = 'camel3118',password = 'Pbldb1234',db = 'banksysdb',charset = 'utf8')
    return conn

def transfer(account, account1, balance):
    
    sql = "SELECT 계좌번호, 예금주, 잔액 FROM 입출금통장 WHERE 계좌번호=%s ORDER BY 거래일 DESC LIMIT 1"
    sql_in = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 보낸분_받는분, 잔액) VALUES(%s,%s,%s,%s,%s)"
    sql_out = "INSERT INTO 입출금통장 (계좌번호, 예금주, 출금액, 보낸분_받는분, 잔액) VALUES(%s,%s,%s,%s,%s)"
    conn = getCon()
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql,(account))
            result = cur.fetchall() # str?
            print(result) # 오류발생
            sum1 = int(result[2])-int(balance)
            print(sum1)
            cur.execute(sql_out, (account, result[1], balance, account, sum1))
            conn.commit()
    
    conn1 = getCon()
    with conn1:
        with conn1.cursor() as cur1:
            cur1.execute(sql,(account1))
            result1 = cur1.fetchone()
            sum2 = int(result[2])+int(balance)
            cur1.execute(sql_in, (account, result1[1], balance, account1, sum2))
            conn1.commit()
    
    
def deposit_out(account, balance):
    conn = getCon()
    try:
        sql = "SELECT 계좌번호, 예금주, 잔액 FROM 입출금통장 WHERE 계좌번호=%s ORDER BY 거래일 DESC LIMIT 1"
        sql_in = "INSERT INTO 입출금통장 (계좌번호, 예금주, 출금액, 보낸분_받는분, 잔액) VALUES(%s,%s,%s,%s,%s)" 
    
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (account))
                result = cur.fetchone()
                
                sum1 = int(result[2])-int(balance)
                cur.execute(sql_in, (account, result[1], balance, result[1], sum1))
                conn.commit()
    except Exception as e:
        print(e,"잘못된 정보입니다.")
            
            
            
deposit_out(1111-1111,1000)
