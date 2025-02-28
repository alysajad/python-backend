my_dict={
    'name':'tim',
    'age':100,
    'is_verified':True,
    'nationality':'kashmiri',
    'city':'srinagar',
    'Qualificationmonth':'january',
    'friends':['peter','list','alice',]

}
print(my_dict['name']) #get the data from the dictionary
#duplicates not allowed in dictionary
#keys cant be same as values
#2 keys cant be same

print(my_dict['age'])
# print(my_dict['dob'])#error
print(len(my_dict))

print(my_dict['is_verified'])
print(type(my_dict))
x=my_dict.get('name')
print(x)