import pandas
import MYSQLBANK as msk
import random
import datetime


def main():
    
    while True:
        menu = input("업무 번호를 입력하세요 1:계좌 개설, 2: 거래 내역 조회, 3:입금, 4:출금, 5:계좌이체, 6:업무종료: ")
        print("2개 이상 항목 입력시 , 로 구분해주세요")
        if menu == "1":
            make = input("개설하실 계좌의 종류를 입력하세요. 입출금통장:1 / 적금통장:2 : ")
            if make == "1": #입출금통장 개설
                
                cmd = input("개설하실 계좌의 계좌번호, 예금주, 생년월일, 비밀번호, 입금액 을 입력하세요.최소 입금액은 1원 입니다: ").split(",")
                
                계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 입금액 = cmd[0], "입출금통장", cmd[1], cmd[2], cmd[3], cmd[4]
                
                msk.create_account_inout(계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 입금액)
                
                print("계좌가 생성되었습니다. 예금주:{}, 계좌번호:{}, 잔액:{}".format(예금주, 계좌번호, 입금액))
                break
            elif make == "2": #적금통장 개설
                
                cmd2 = input("개설하실 계좌의 계좌번호, 예금주, 생년월일, 비밀번호, 입금액 을 입력하세요.최소 입금액은 1원 입니다: ").split(",")
                
                계좌번호2, 계좌형태2, 예금주2, 생년월일2, 비밀번호2, 입금액2 = cmd2[0], "적금통장", cmd2[1], cmd2[2], cmd2[3], cmd2[4]
                
                time= datetime.datetime.now()+datetime.timedelta(days=730)
                
                만기일 = time.strftime("%y-%m-%d")
                
                msk.create_account_saving(계좌번호2, 계좌형태2, 예금주2, 생년월일2, 비밀번호2, 입금액2, 만기일)
                
                print("적금계좌가 생성되었습니다. 예금주:{}, 계좌번호:{}, 잔액:{}".format(예금주2, 계좌번호2, 입금액2))
                
                break
            else:
                print("잘못된 값을 입력하였습니다")
        elif menu == "2":
            make = input("조회하실 계좌의 종류를 입력하세요 입출금통장:1, 적금통장:2 : ")
            if make == "1":
                made = input("조회하실 계좌번호를 입력하세요: ")
                msk.search_inout_account(made)
                break
            elif make == "2":
                made = input("조회하실 계좌번호를 입력하세요: ")
                msk.search_saving_account(made)
                break
            else: 
                print("잘못된 입력값 입니다.")
        elif menu == "3":
            make = input("입금하실 계좌의 종류를 입력하세요 입출금통장:1, 적금통장:2 : ")
            if make == "1":
                made = input("입금하실 계좌번호와 입금액을 입력하세요: ").split(",")
                msk.deposit_in(made[0], made[1])
                print(("계좌 {}에 {}원이 입금되었습니다").format(made[0], made[1]))
                break
            elif make == "2":
                made = input("입금하실 계좌번호와 입금액을 입력하세요: ").split(",")
                msk.saving_in(made[0], made[1])
                print(("계좌 {}에 {}원이 입금되었습니다").format(made[0], made[1]))
                break
                
        elif menu == "4":
            make = input("출금하실 계좌의 계좌번호와 출금액을 입력하세요: ").split(",")
            msk.deposit_out(make[0], make[1])
            print(("계좌 {}에 {}원이 출금되었습니다").format(make[0], make[1]))
            break
            
        elif menu == "5":
            make = input("출금하실 계좌의 계좌번호와 이체하실 계좌번호, 이체금액을 입력하세요: ").split(",")
            msk.transfer(make[0], make[1], make[2])
            print(("계좌 {}에 {}원이 이체되었습니다").format(make[1], make[2]))
            break
            
        elif menu == "6":
            print("업무가 종료됩니다")
            break
        else: 
            print("잘못된 입력값 입니다.")
        
            
main()