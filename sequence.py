n = int(input("Enter the length of the sequence: ")) # Do not change this line

sum1 = 1
sum2 = 2
sum3 = 3
print(sum1)
print(sum2)
print(sum3)

for i in range(1,n-2):
    summa = sum1+sum2+sum3
    sum1 = sum2 
    sum2 = sum3
    sum3 = summa

    print(summa)