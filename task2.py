#Remove duplicate character in given string
a=input()
val=''
for i in a:
   if i not in val:
      val=val+i
print(val)

#Rotate array left by k times
arr=[1,2,3,6,7,8]
k=int(input("Enter value of k:"))
print("Before left shift array:",arr)
for i in range(k):
   temp=arr[0]
   for j in range(len(arr)-1):
       arr[j]=arr[j+1]

   arr[len(arr)-1]=temp
print("After left shift array",arr)

#Rotate array right by k times
arr=[1,2,3,6,7,8]
k=int(input("Enter value of k:"))
print("Before right shift array:",arr)
for i in range(k):
    temp=arr[len(arr)-1]
    for j in range(len(arr)-1,-1,-1):
         arr[j]=arr[j-1]
    arr[j]=temp
print("After Right shift array:",arr)

#shift all zeros into right side in given array
list1=[1,2,0,5,0,6,0,4]
print("Before shifting all zero in right side",list1)
count=0
for i in range(len(list1)):
    if(list1[i]!=0):
        list1[count]=list1[i]
        count=count+1
while count<len(list1):
    list1[count]=0
    count=count+1
print("After shifting all zero in right side",list1)


#find kth smallest element
arr=[2,4,5,21,77,34]
print("Original list",arr)
k=int(input("enter value of k"))
for i in range(len(arr) - 1):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("kth smallest element",arr[k-1])