import pymysql
import datetime
import pandas as pd


create = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액) VALUES (%s,%s,%s,%s,%s,%s)"
create_sa = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액, 만기해지일) VALUES (%s,%s,%s,%s,%s,%s,%s)"
in_out_create = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 잔액) VALUES (%s,%s,%s,%s)"
saving_create = "INSERT INTO 적금통장 (계좌번호, 예금주, 입금액, 잔액, 만기일) VALUES (%s,%s,%s,%s,%s)"

def getCon():
    conn = pymysql.connect(host= 'localhost', port=3306, user = 'camel3118',
                        password = '373954',
                        db = 'Bankdb',
                        charset = 'utf8')
    return conn


def create_account_inout(account, kind, name, birth_date, pw, balance):
    conn = getCon()
    with conn:
        with conn.cursor() as cur:
            cur.execute(create, (account, kind, name, birth_date, pw, balance))
            conn.commit()
    conn2 = getCon()
    with conn2:
        with conn2.cursor() as cur:
            cur.execute(in_out_create, (account, name, balance, balance))
            conn2.commit()
    
    
def create_account_saving(account, kind, name, birth_date, pw, balance, expire_date):
    conn = getCon()
    with conn:
        with conn.cursor() as cur:
            cur.execute(create_sa, (account, kind, name, birth_date, pw, balance, expire_date))
            conn.commit()
    conn2 = getCon()
    with conn2:
        with conn2.cursor() as cur:
            cur.execute(saving_create, (account, name, balance, balance, expire_date))
            conn2.commit()




def search_inout_account(account):
    search_inout = "SELECT 거래일, 계좌번호, 입금액, 출금액, 보낸분_받는분, 잔액 FROM 입출금통장 WHERE 계좌번호=%s ORDER BY 거래일 DESC"
    conn = getCon()
    with conn:
        with conn.cursor() as cur:
            cur.execute(search_inout, (account))
            result = cur.fetchall()
            for data in result:
                print(data)

    
                
def search_saving_account(account):
    conn = getCon()
    search_saving = ("SELECT 거래일, 계좌번호, 입금액, 잔액 FROM 적금통장 WHERE 계좌번호={} ORDER BY 거래일 DESC").format(account)
    with conn:
        with conn.cursor() as cur:
            cur.execute(search_saving, (account))
            result = cur.fetchall()
            for data in result:
                print(data)
            
def deposit_in(account, balance):
    conn = getCon()
    try:
        sql = "SELECT 계좌번호, 예금주, 잔액 FROM 입출금통장 WHERE 계좌번호=%s ORDER BY 거래일 DESC LIMIT 1"
        sql_in = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 보낸분_받는분, 잔액) VALUES(%s,%s,%s,%s,%s)" 
    
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (account))
                result = cur.fetchone()
                
                sum1 = int(result[2])+int(balance)
                cur.execute(sql_in, (account, result[1], balance, result[1], sum1))
                conn.commit()
    except Exception as e:
        print(e,"잘못된 정보입니다.")



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




        
def saving_in(account, balance):
    conn = getCon()
    try:
        sql = "SELECT 계좌번호, 예금주, 잔액, 만기일 FROM 적금통장 WHERE 계좌번호=%s ORDER BY 거래일 DESC LIMIT 1"
        sql_in = "INSERT INTO 적금통장 (계좌번호, 예금주, 입금액, 잔액, 만기일) VALUES(%s,%s,%s,%s,%s)" 
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (account))
                result = cur.fetchone()
                
                sum1 = int(result[2])+int(balance)
                cur.execute(sql_in, (account, result[1], balance, result[1], sum1, result[3]))
                conn.commit()
    except Exception as e:
        print(e,"잘못된 정보입니다.")


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

