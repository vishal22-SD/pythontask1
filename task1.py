

# WAP print following output to screen:
print("{}{}".format("Escape character","Use"))
print("{}{}".format("/n","Newline"))
print("{}{}".format("/t","Space/tab"))
print("{}{}".format("\'","Single Quote"))
print("{}{}".format("\"","Double Quote"))

# WAP to swap two numbers
val1=5
val2=6
temp=val1
val1=val2
val2=temp
print(val1,val2)

# WAP to accept student details rollno,name,percentage and display in given format.
Name=input()
Rollno=int(input())
percentage=float(input())
print("{} {} {}".format("Rollno","Name","Percentage"))
print("{} {} {}".format( Rollno, Name, percentage))

#Write a menu driven program to calculate prime,factorial,amstrong,palindrome number.

def checkprime(n):
  if(n<=1):
    return "Not prime"
  else:
    for i in range(2,(n//2+1)):
      if(n%i==0):
        return "Not Prime"
      else:
        return "Prime"
def checkFactorial(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
def checkPalindrome(n):
  val=n
  rev=0
  while(n!=0):
     rem=n%10
     rev=rev*10+rem
     n=n//10
  if(rev==val):
    return "yes palindrome"
  else:
    return "Not palindrome"
def checkamstrong(n):
  val=n
  length=len(str(n))
  rev=0
  while(n!=0):
     rem=n%10
     rev=rev+(rem**length)
     n=n//10
  if(rev==val):
    return "yes "
  else:
    return "No"


while True:  
    print("\nMAIN MENU")  
    print("1. Check number is Prime or not")  
    print("2. Check number of factorial")  
    print("3. Check number is palindrome or not")  
    print("4. Check number is amstrong or not") 
    print("5. Exit") 
    num = int(input("Enter the Choice:")) 
    if (num==1):
      value=int(input())
      print(checkprime(value))
    if (num==2):
      value=int(input())
      print(checkFactorial(value))
    if (num==3):
      value=int(input())
      print(checkPalindrome(value))
    if (num==4):
      value=int(input())
      print(checkamstrong(value))
    if (num==5):
      break

# Wap to calculate cube of number in given range
for i in range(2,5+1):
   print(i,':',i**3)
print()

#WAP given string is palindrome
def palindrome(n):
   val = ''
   val=val+n[::-1]
   if (val == n):
      print("palindrome")
   else:
      print("Not palindrome")
str1=input()
palindrome(str1)

#wap to find largest common subsquence
def lcs(val1, val2, len1, len2):
  
    if len1== 0 or len2 == 0:
       return 0;
    elif val1[len1-1] == val2[len2-1]:
       return 1 + lcs(val1, val2, len1-1, len2-1);
    else:
       return max(lcs(val1, val2, len1, len2-1), lcs(val1, val2, len1-1, len2));
str1 =input()
str2 =input()
print ("Length of LCS is ", lcs(str1, str2, len(str1), len(str2)))