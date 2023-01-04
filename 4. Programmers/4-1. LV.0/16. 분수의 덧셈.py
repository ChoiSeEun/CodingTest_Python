def reduction(answer):
    max_num = min(answer)
    i = 2 
    while (i<=max_num):
        if answer[0]%i == 0 and answer[1]%i ==0:
            answer[0] = answer[0]//i
            answer[1] = answer[1]//i 
            i = 2
            max_num = min(answer)
        else:
            i += 1
    return answer 

def solution(denum1, num1, denum2, num2):
    denum1 *= num2
    denum2 *= num1
    answer= []
    answer=[denum1+denum2,num1*num2]
    answer = reduction(answer)
    return answer
