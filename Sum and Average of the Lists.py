num =1
list =[]
sum = 0
avg =-1

while (num!=0):
    num= int(input("Enter the number"))
    list.append(num)
    
    sum = sum+num
    avg = avg+1
   

print( "Sum = " ,sum)
print("Average =" ,sum/avg)
list.pop()
print(list)
