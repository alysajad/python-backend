def greetings_func(name):
    print('welcome',name)#python is dependendt on intendation
    print("How are you?")   #python is dependendt on intendation

greetings_func('ali')#function call
#functions are used to avoid repetition of code
#functions are used to make the code more readable
#functions are used to make the code more reusable
#functions are used to make the code more reliable 
#can be multiparametrized also
def greeting(*names):
    print('welcome',names[1])#python is dependendt on intendation

greeting('ali','ahmed','khan')#function call
# Compare this snippet from dictionaries.py:
def myfunc():
    return 5+4
print(myfunc())
#functions are used to avoid repetition of code
def addno(num1,num2):
   return num1+num2
print(addno(4,9))

#we dont write anything after return
