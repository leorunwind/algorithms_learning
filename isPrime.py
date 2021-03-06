def isPrime(num):
    #判断一个数是否为素数的超高效率算法
    if num <= 3:
        return num>1
    
    if num%2==0 or num%3==0:
        return False
    
    #步长为6---5, 6, 7, 8, 9, 10,是一个循环里要考虑的数，
    #6,8,9,10都可以分解为2*x，或者3*x，然后步长再加6， 6可以分解为2*3， 所以加起来是2*（x+3），或者3*（x+2）
    #因此只需考虑能否被i和i+2整除
    i = 5
    while(i*i <= num):
        if(num%i == 0 or num%(i+2) == 0):
            return False
        i += 6
    return True
        
#打印1000以内的素数
for i in range(1000):   
    if(isPrime(i)):
        print(i),
