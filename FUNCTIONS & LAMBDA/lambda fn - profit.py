#i=pnr p=3000 , r=.6 , n=4

interst=lambda p,n,r:p*n*r
n1=int(input("Principal"))
n2=int(input("Number of years"))
n3=float(input("Rate of interest"))
print("Interest",interst(n1,n2,n3))


# interst=lambda p,n,r:p*n*r
# print("Interest",interst(3000,4,.6))

