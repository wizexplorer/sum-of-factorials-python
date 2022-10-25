print("|-------------------------EXPERIMENT NO.14-----------------------------|")
print("|            FINDING SUM FROM 1! TO GIVEN NUMBER                |")
print("*"*72)
piggy=0
N=eval(input("    Enter the terms you want for the series : "))
print("","\n\t\t\t",end="")
for n in range(1,N+1):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    if n<N:
        print(n,"!",end="+",sep="")
    else:
        print(n,"!",end=" = ",sep="")
    piggy=piggy+fact    
print(piggy)
print("")
print("*"*72)
