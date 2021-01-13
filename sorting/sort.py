# this is the simple code to do the sorting of the list or array.


l=[5,4,3,2,1,12,99]

# Bubble sort

for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp

print(l)

# we can also use the inbuilt functions as well

print(sorted(l))