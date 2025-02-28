
countries=['united kingdom','ghana','kashmir','baramulla',]
print(countries)
print(countries[2])
print(countries[1:3])#print range
print(type(countries))
countries[0]='india'#replace
print(countries)
#get end of the list
print(countries[-1])#last
print(countries[-2])#2nd last


#list mwethods
countries=list(('nigeria',False,34))
list1=[1,2,3,4,5,6,7,8,9,10]
list2=['banana','apple','mango','orange']
list1.extend(list2)#extend
print(list1)
list2.append('cherry monkey')#append
print(len(list2))
list2.insert(1,'grapes')#insert
print(list2)
list2.remove('banana')#remove
print(list2)
list2.pop()#pop
print(list2)
list2.pop(3)#pop
print(list2.index('mango'))#index
list2.reverse()#reverse

print(list2.count('mango'))#count

list3=list2.copy()#copy
del list2#delete    
