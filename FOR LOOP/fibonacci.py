#fibonacci series
#0 1 1 2 3 5 8 13 21.......n

n=int(input('Enter limit'))
f=0
s=1
print(f,s)
for i in range(2,n):
    t=f+s                  #t=0+1           t=1+1=2              t=1+2=3      .....
    print(t)               #1                 2                   3           .....
    f=s                    #f=1               f=1                 f=2         .....
    s=t                    #s=1               s=2                 s=3         .....