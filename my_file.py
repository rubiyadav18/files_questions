a=[1,2,3,4,5,6,7,8,9,10]
f=open("int.txt","w")
i=0
while i<len(a):
    c=str(a[i])
    f.write(c)
    f.write("\n")
    i=i+1
f.close()
f=open("int.txt","r")
print(f.read())
f.close()