def float_check(nums):
        try:
            int(nums)
                
            print("입력값:{} , "정수" 입니다.".format(nums))
        except:
            try:
                if "." in nums:
                    try:
                        float(nums)
                        print("입력값:{} , "실수" 입니다.".format(nums))
                    except:
                        print("입력값:{} , "숫자"가 아닙니다.".format(nums))
            except:
                print("입력값:{} , 숫자가 아닙니다.".format(nums))
            
float_check(input("숫자를 입력하세요: "))