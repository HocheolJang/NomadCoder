
#Python으로 웹 스크래퍼 만들기

# 1.8 Code Challenge
# 7가지 function 만들기
# plus, minus, times, division, negation, power, reminder

def plus(a=0, b=0):
    return float(a + b)

def minus(a=0, b=0):
    return float(a - b)

def times(a=0, b=0):
    return float(a * b)

def division (a=0, b=0):
    return float(a / b)

def negation (a=0):
    return -float(a)

def power (a=0, b=0):
    return pow(a, b)

def reminder(a=0, b=0):
    return int(a % b)

print(plus(2.3, 4.23))
print(minus(2))
print(times(2,3))
print(division(3,4))
print(negation(2))
print(power(3,2.4))
print(reminder(3, 3))