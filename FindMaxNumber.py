numbers=input("Please enter number String : " )
temp=0
length1= numbers.split(",")
l1=len(length1)
numbers=input(numbers)
print(numbers)
for i in range(0,l1-1):
    for j in range(0,l1-1):
        if numbers[i]  < numbers[j] :
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = numbers[i]
print(numbers)
