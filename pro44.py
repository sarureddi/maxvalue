h1,m1,d1,s1=map(int,input().split())
n1=[int(i) for i in input().split()]
a=[m1*n1[i]+d1*n1[j]+s1*n1[k] for i in range(len(n1)) for j in range(len(n1)) for k in range(len(n1)) if i<=j<=k]
print(max(a))
