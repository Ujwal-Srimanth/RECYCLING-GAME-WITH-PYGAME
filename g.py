# cook your dish here
t=int(input())
while(t!=0):
    list1=[]
    count=0
    cost=0
    x, y = [int(x) for x in input().split()]
    m=input()
    lum=m.count('1')
    cost=cost+lum*x
    i=0
    while(i<len(m)):
        if(i==len(m)-1 and m[i]==1):
            count=count+1
            list1.append(count)
        elif(m[i]=='1'):
            count=count+1
        else:
            list1.append(count)
            count=0
            a=m[i]
        i=i+1
    z=max(list1)
    cost=cost+z*y
    print(cost)
    t=t-1
