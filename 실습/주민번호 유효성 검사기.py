#주민등록번호 유효성 검사기

#주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성
#을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2,
#3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지
#가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

# def로 함수화 하여 사용???



# 입력은 한번만
# if 문

while True:

    first_regi = input("주민등록번호(하이픈 포함)를 입력하세요: ")

    if len(first_regi) == 14:
        regi = first_regi.replace("-","")
        try:
            int(regi)
            break
        except:
            print("2잘못된 값을 입력하였습니다")
        
    else:
        print("1잘못된 값을 입력하였습니다.")
    
    
            
    
print()
print("정상 입력되었습니다")


regi1 = list(map(int,regi))



num1 = [2,3,4,5,6,7,8,9,2,3,4,5]



i_result = []

for i in regi1:
    for j in num1:
        i_result.append(i*j)

        
sum1 = sum(i_result)

div1 = sum1/11

n_result = div1-11

if n_result == regi1[11:]:
    print(first_regi, "유효한 주민등록번호 입니다",end="\n")
else:
    print(first_regi, "유효하지 않은 주민등록번호 입니다",end="\n")


