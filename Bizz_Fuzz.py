count=1
count1=1

print("Type a value of 'N' you want to print up to, ( Eg: 30 ) otherwise simply press enter to make default ( N=17 )")
print("")
print("N = ",end='')
y=input()
print("")

if y!="":
    N=int(y)
else:
    N=18

for n in range(1,N):
       if n == 3 * count and n == 5 * count1:
           print("FizzBuzz,", end='')
           count+=1
           count1+=1
       elif n==3*count:
           print("Fizz,",end='')
           count+=1
       elif n==5*count1:
           print("Buzz,",end='')
           count1+=1
       else:
           print(str(n)+',',end='')
print("")
print("")
print("Press enter to exit the program")
input()