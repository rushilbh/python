file1=input("Enter your file name:-")
f=open(file1,'r')
fileContents=f.read()
print(fileContents)

file2=input("Enter file 2 pls:-")
g=open(file2,'r')
fileContents2=g.read()
print(fileContents2)


f=open(file1,'w')
g=open(file2,'w')

f.write(fileContents2)
g.write(fileContents)

f.close()
g.close()
