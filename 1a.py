m1=int(input("Enter a number:"))
m2=int(input("Enter a number:"))
m3=int(input("Enter a number:"))
if(m1<m2 and m1<m3):
    Avg=(m2+m3)/2
elif(m2<m1 and m2<m3):
    Avg=(m1+m3)/2
elif(m3<m1 and m3<m2):
     Avg=(m1+m2)/2
print("Average of 2 marks is",Avg)
