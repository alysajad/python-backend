# try except 
try:
    x = int (input ('input integer'))
    print(x)
except ValueError: # error in the type of value passed
    print('value not an integer')
else: print('nothing wents weong')

finally: print('try except finnish excep')


