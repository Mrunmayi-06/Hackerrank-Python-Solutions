n=int(input())#takes n as input
if n%2!=0:
    print("Weird")#prints weird if n is odd
else :
       if 2<=n<=5:#prints Not Weird If n is even and in the inclusive range of 2 to 5
           print("Not Weird")
       elif 6<=n<=20:#prints Not Weird If n is even and in the inclusive range of 6 to 20
           print("Weird")
       else:#prints Not Weird If n is even and greater than 20
           print("Not Weird") 