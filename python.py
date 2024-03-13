# x=1
# sum=0
# while x<10:
#     sum=sum+x
#     x=x+1
#     x=1

#     product = 1
#     while x<10:
#         product = product*x
#         x=x+1

#         print(sum,product)

# n=2
# i=0
# while True:
#     print('{}^{}={}'.format(n,i,n**i))
#     if i>21: break
#     i+=1 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")