amount = 0



try:
    amount = int(input('please type the yearly package: '))
    months = int(input('please type the number of months: '))
    salary = int((amount/months))

except ValueError:
    print('enter only numerical values')

except ZeroDivisionError:
    print('please type the months between 1 to 12')

except Exception:
    print('there is something wrong in the provided details please check and try again later')

finally:
    print (f'the salary in months for {amount} L.P.A is {salary}')

