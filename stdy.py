# print("select")
# print("add")
# print("sub")
# print("div")
# print("mult")
#
# op=input()
# if op=="2":
#     x=int(input("enter the 1st number:"))
#     y=int(input("enter the 2nd number:"))
#     print("add is" + str(int(x)+int(y)))
#
# elif op=="3":
#     x=int(input("enter the 1st number:"))
#     y=int(input("enter the 2nd numbewr"))
#     print("sub is " + str(int(x)-(y)))

# largets no nested if

# x=int(input("enter the 1st number:"))
# y=int(input("enter the 2ndt number:"))
# z=int(input("enter the 3rd number:"))
#
# if x>y:
#     print(x ,"is the largest no")
#
#     if x>z:
#         print(x ," is the largest number")
#
#     if y>x:
#         print(y ,"is largest number")
#         if y>z:
#             print(y, "is largest number")
# else:
#     print(z, "is the largest number"
#

# print natural no reverse using while loop
# n=int(input("enter the no:"))
#
# # while n>=0:
# #     print(n)
# #     n=n-1

# programme check the no given prime or not using for loop
# n=int(input("enter  the no:"))
# for i in range(2,n):
#     if n%i==0:
#         print(n,"is not a prime number")
#         break
# else:
#     print(n,"is a prime number")

# fibonacci series
# n=int(input("enter the fibonacci sequence:"))
# n1=0
# n2=1
# i=0
# if n<0:
#     print("enter positive values")
# elif n==1:
#     print(n1)
# else:
#     print(n1)
#     print(n2)
#     while i<n:
#         n3=n1+n2
#         print(n3)
#         n1=n2
#         n2=n3
#         i=i+1

#check even no using for loop
# for i in range(2,21,2):
#     print(i)

# check sum of natural numbers using for loop
# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum=i+sum
#     print(sum)

# multiplication using for loop

# n=(int(input("entr the no:")))
# for i in range(1,11):
#     print(i,'*',6,'=',n*i)

# reverse using for loop 0 to 10
# n=int(input("enter a no:"))
# for i in range(10,-1,-1):
#     print(i)

#nested for loop inside for loop
# a=[1,2]
# b=[3,4]
# for i in a:
#     for j in b:
#         print(i,j)

#multip[ly 2 to 5 using nested for loop
# for i in range(2,6):
#     for j in range(1,11):
#         mul=i*j
#         print(i,'*',i,j,'=',mul)

# prod to find smallest number from list
# list=[1,3,57,5,56]
# smallestnum=list[0]
# for i in list:
#     if smallestnum>i:
#         smallestnum = i
#
# print("smallestnum is" ,smallestnum)

#print hollow square pattern using alphabets in python

# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         ch=chr(64+i)
#         if(i==1 or i==n or j==1 or j==n):
#             print(ch,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# programme the name python using hollow square pattern
# word=(str(input("enter the word")))
# leng=len(word)
# for i in range(0,leng):
#     if i==0 or i==leng-1:
#         print(leng *(word[i]+' '))
#     else:
#         print(word[i]+((leng-2)*'  ')+' '+word[i])

#programme a design of the 1st letter of your name as M
for i in range(7):
    for j in range(7):
        if j==0 or j==6 or(i==j) and (j>0 and j<4) or(i==1 and j==5) or (i==2 and j==4):
            print('*',end=' ')
        else:
            print(end='  ')
    print( )