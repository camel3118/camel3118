import random
import pickle

def load_account():
    data1 = []
    with open("account.pkl", "rb") as np:
            while True:
                try:
                    data = pickle.load(np)
                except EOFError:
                    break
                data1.append(data)
    return data1
                
def load_name():
    data2 = []
    with open("name.pkl", "rb") as np:
            while True:
                try:
                    data = pickle.load(np)
                except EOFError:
                    break
                data2.append(data)
                
    return data2

def load_balance():
    data3=[]
    with open("balance.pkl", "rb") as bl:
            while True:
                try:
                    data = pickle.load(bl)
                except EOFError:
                    break
                data3.append(data)
                
    return data3
    

class Account:
    
    def __init__(self, name=0, number=0, balance=0):
        
        self.name = name
        self.namelist = []
        self.accountlist = []
        self.balancelist = []
        self.number = number
        self.balance = balance
        
    
    def find_account(self,number): # 여기 
        
        data1 = load_account()
        data2 = load_name()
        data3 = load_balance()
        
        
        try: 
            print(data1, type(data1))
            print(data2,type(data2))
            print(len(data1))
            for i in range(len(data1)):
                p = 0
                while p <= len(data1):
                    p += 1
                    if number != data1[i]:
                        continue
                    else:
                        result_num = data1[i]
                        print("조회결과 계좌번호:{}, 예금주:{}, 잔액 {} 입니다.".format(result_num,data2[i], data3[i]))
                        
                        break
        except Exception:
            raise

        
    def new_account(self,number,name,balance):
        
        self.accountlist.append(number)
        self.namelist.append(name)
        self.balancelist.append(balance)
        with open("account.pkl", "ab") as ac:
            for a in self.accountlist:
                pickle.dump(a, ac)
            
        with open("name.pkl","ab") as na:
            for b in self.namelist:
                pickle.dump(b,na)
                
        with open("balance.pkl","ab") as bl:
            for c in self.balancelist:
                pickle.dump(c,bl)
    
    
class Bank(): 

        
        
    def deposit(self, number, amount):
        data1 = load_account()
        
        data3 = load_balance()
        
        # 계좌번호 인덱스 찾기
        for i in range(len(data1)):####
            p = 0
            while p <= len(data1):
                p += 1
                if number != data1[i]:
                    continue
                else:
                    result_num = i
                    
                    break
                    
        
        
        if amount >= 1:
            a = int(data3[result_num]) + amount
            print(a)
            data3.insert(result_num, a)
        
        print("입금이 완료되었습니다. 잔액:{}".format(a))
            
        with open("balance.pkl","wb") as bl:
            for c in data3:
                pickle.dump(c,bl)
            
    def withdraw(self, number, amount):
        data1 = load_account()
        data3 = load_balance()
        
        
        for i in range(len(data1)):
            p = 0
            while p <= len(data1):
                p += 1
                if number != data1[i]:
                    continue
                else:
                    result_num = i
                    
                    break
                    
        
        
        if amount >= 1:
            a = int(data3[result_num]) - amount
            data3.insert(result_num, a)
        
        print("출금이 완료되었습니다. 잔액:{}".format(a))
            
        with open("balance.pkl","wb") as bl:
            for c in data3:
                pickle.dump(c,bl)
                
                
    def transfer(self, number_tran, amount):
        
        
        data1 = load_account()
        
        data3 = load_balance()
        
        for i in range(len(data1)):
            p = 0
            while p <= len(data1):
                p += 1
                if number_tran != data1[i]:
                    continue
                else:
                    result_num = i
                    
                    break
                    
        if amount >= 1:
            a = int(data3[result_num]) + amount
            print(a)
            data3.insert(result_num, a)
        
        
            
        with open("balance.pkl","wb") as bl:
            for c in data3:
                pickle.dump(c,bl)
        print("{}원이 이체되었습니다.".format(a))
    
            
        
def main():
    bank = Bank()
    account = Account()
    while True:
        menu = input("업무 번호를 입력하세요 1:계좌 개설, 2: 계좌 조회, 3:입금, 4:출금, 5:계좌이체, 6:업무종료: ")
        print("2개 이상 항목 입력시 , 로 구분해주세요")
        if menu == "1":
            cmd = input("개설하실 계좌의 예금주, 계좌번호, 입금액을 입력하세요. 최소 입금액은 1원 입니다: ").split(",")
            name, number, balance = cmd[0], cmd[1], int(cmd[2])
            account.new_account(number=number, name=name, balance=balance)
            print("계좌가 생성되었습니다. 예금주:{}, 계좌번호:{}, 잔액:{}".format(name,number,balance))
            break
        elif menu == "2":
            cmd = input("조회하실 계좌의 계좌번호를 입력하세요: ")
            number = cmd
            a1 = account.find_account(number)
            return a1
        elif menu == "3":
            cmd = input("입금하실 계좌번호와 금액을 입력하세요: ").split(",")
            number, amount = cmd[0], int(cmd[1])
            b1 = bank.deposit(number=number, amount=amount)
            return b1
            
        elif menu == "4":
            cmd = input("출금하실 계좌번호와 금액을 입력하세요: ").split(",")
            number, amount = cmd[0], int(cmd[1])
            c1 = bank.withdraw(number=number, amount=amount)
            return c1
        
        elif menu == "5":
            cmd = input("출금하실계좌, 이체를 원하시는금액(1원 이상)을 입력하세요: ").split(",")
            cmd1 = input("받으시는계좌를 입력하세요: ")
            number, amount, number_tran = cmd[0], int(cmd[1]), cmd1
            d1 = bank.withdraw(number=number, amount=amount)
            e1 = bank.transfer(number_tran=number_tran, amount=amount)
            return d1, e1
            
        elif menu == "6":
            print("업무를 종료합니다")
            break
            
        else:
            print("잘못된 명령어 입니다.")
            break
            
main()

