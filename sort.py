n=int(input())
l=[]
for i in range (n):
    l.append(int(input()))
k=sorted(l)
print((" ".join((map(str,k)))))
