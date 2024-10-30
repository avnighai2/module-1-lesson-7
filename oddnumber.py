n = int(input(" Enter the number:"))
sum = 0 


#for i in range( 10, n+1, 2):
#   sum = sum + i
#  print(i)
# print(f" The sum of odd digits is {sum}")


for i in range(10, n, 1 ):
  if i % 2 == 0: #for odd  n % 2 == 1 
        sum = sum + i
        print(i)

print(f" The sum of {n} odd number is {sum}")

