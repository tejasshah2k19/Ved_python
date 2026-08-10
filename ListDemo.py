"""
    list - python's built-in collection / data structures 
    
    ordered 
    mutable 
    allow duplicates 
    allow difference data types 
    supports indexing 
    supports negative indexing 
    supports slicing 
    dynamic size 
    coniguous memory allocation 
    supports iteration 
    supports nested list 

"""




list = [] 
# myList = list() 

x = [10,20,30,40,50,20]  #duplicate allow 

print(x)

y = [10,20,'rock']



#append 
for i in range(6):
    print("Enter name")
    name = input()
    list.append(name)

print(list)

for data in list:
    print(data)
    



list=[1,2,3]

myData = [] 

# myData.push(12)   #not available  


myData.append(10)
myData.append(20)



myData.extend(list) #[10 20 1 2 3 ] 

myData.append(list) #[10 20 [1,2,3] ] 


#insert 


myList = [10,20,30,40,50]

myList.insert(1,300)


print(myList) #[10,300,20,30,40,50]

#append extend insert 


#remove , pop , clear 
myList.remove(20) # value 
myList.pop() # remove last item  -> return removed item 
myList.pop(0) # remove 0th index -> 
myList.clear() # remove all the items 


myList = [10,20,30,40,30,20,400]
print(myList[0])

#search 
print(myList.index(20)) #search 20 and return the index of 20 -> first occurence 
print(myList.index(20,6)) #search 20 from 6th index and return the index of 20 
print(myList.index(20,6,9)) #search 20 from 6th index to 9th index and return the index of 20 


#count 
myList.count(20) # count how many times 20 presnt in list and return 

#sort 
myList.sort() # original list will modify 
myList.sort(reverse=True)

#reverse 
myList.reverse() 



"""
time complexity 


append          O(1) amortized 
pop()           O(1)
insert()        O(n)
remove()        O(n)
index()         O(n)
count()         O(n)
sort()          O(n log n)
reverse()       O(n)

python -> list -> sort() -> TimSort 

    hybrid sorting algorithm -->
                    Merge + insertion 
                    
    Best Case O(n)
    Worst Case O(n log n)


"""




