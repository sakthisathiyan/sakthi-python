a=[]
print("enter 10 number:")
for i in range(1,11):
    num=int(input("enter num "+str(i)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)
