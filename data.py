my_file=open("data.text","r")
file1=open("delhi.text","w")
file2=open("shimla.text","w")
file3=open("other.text","w")
for data in my_file:
    if "delhi" in data:
        file1.write(data)
    elif "shimla"in data:
        file2.write(data)
    else:
        file3.write(data)
file1.close()
file2.close()
file3.close()