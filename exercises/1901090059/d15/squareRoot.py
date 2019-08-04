# 计算从终端输入一个数的平方根

def squareRoot1(x = 25):
    epsilon = 0.01
    step = epsilon**3
    numGuesses = 0
    ans = 0.0
    while abs(ans**2 -x) >= epsilon and ans*ans <= x:
        ans += step
        numGuesses += 1
    print('numGusses = ', numGuesses)
    if abs(ans**2 - x) >= epsilon:
        print('Failed on square root of', x)
    else:
        print(ans, 'is close to square root of ', x)

def squareRoot2(x = 25):
    epsilon = 0.01
    numGuesses = 0
    low = 0.0 
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**2 -x ) >= epsilon:
        print('low =', low, 'high = ', high, 'ans = ', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans 
        else:
            high = ans
        ans = (high + low ) / 2.0
    print('numGuesses = ', numGuesses)
    print(ans, 'is close to square root of ', x)

def NewtonRaphson( x = 25):   # for square root
    epsilon = 0.01 
    guess = x/2.0
    numGuessed = 0
    while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))
        numGuessed += 1
    print('Squae root of ', x, 'is about ', guess, 'numGuesses = ', numGuessed)


def addMystery():
    x = 0.0 
    for i in range(10):
        x = x +0.1
    if x == 1.0:
        print(x, '= 1.0')
    else:
        print(x, 'is not 1.0')

def main():
    squareNR = NewtonRaphson(123456)
    squareRot = squareRoot2(123456)
    
if __name__ == '__main__':
    main()

