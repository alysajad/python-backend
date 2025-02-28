num2=int(input('enter the 2nd num'))
num1=int(input('enter the number'))

op= input('enter the operator\n')
if op=='+':
    print(num1+num2)
elif op=='-':   print(num1-num2)    
elif op=='*':   print(num1*num2)
elif op=='/':   print(num1/num2)
else:
    print('invalid operator')   