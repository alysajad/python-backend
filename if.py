a=7
b=3
if a>b: 
    print(str(a)+' is greater than '+str(b))

else:
    print(str(b)+' is greater than '+str(a))
# Compare this snippet from sets.py:
if a==b: print('a is equal to b')
elif a>b: print('a is greater than b')
# Compare this snippet from strings.py:

if a>=b:
    print('true')
# Compare this snippet from if.py:
boy=True
short=True
if boy==True:
    print('he is  BOY')\
    
if boy==False or short==False:## AND OR WE CAN USE IN PYTHON

    print('he isSHRY')


value = input('input a value \n')
if type(value)==str:
    print(value+' is a string') 
elif type(value)==int:
    print(value+' is an integer')   
elif type(value)==list:
    print(value+' is a list')
else:print('unknown data type')
# Compare this snippet from loops.py:
#here we can change the string into an int by using int before the input
# value = int(input('input a value \n'))    


value=int(input('enter the number'))
if value%5==0:
    print('number is divisible by 5')

 
else:
   print('not divisible by 5')
