#attempting calculator    COMPLETE
print('Pick 1 to add')
print('Pick 2 to subtract')
print('Pick 3 to multiply')
print('Pick 4 to multiply')
begin = int(input('select a number: '))
num1 = int(input('pick first number: '))
num2 = int(input('pick second number: '))


def add(num1, num2):       
    while begin == 1:
        return num1 + num2
    else:
        while begin == 2:
            return num1 - num2
        else:
            while begin == 3:
                return num1 * num2
            else:
                while begin == 4:
                    return num1 / num2
                
print(add(num1, num2))

