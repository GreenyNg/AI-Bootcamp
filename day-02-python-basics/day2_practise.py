# num = int(input("Enter a number: "))

# Determine if the number is positive, negative, or zero
# if num > 0:
#     print(num, "is a positive number.")
#     if num == 0:
#         print(num, "is zero.")
# else:
#     print(num, "is a negative number.")

# Determine if the number is odd or even
# if num >= 1:
#     if num % 2 == 0:
#         print(num, "is an even number.")
#     else:
#         print(num, "is an odd number.")
# else:
#     print(num, "is not greater than or equal to 1 and therefore not an integer.")

# Determine if the number is divisible by 3, 5, or both
# if num % 3 == 0 and num % 5 == 0:
#     print(num, "is divisible by both 3 and 5")
# elif num % 3 == 0:
#     print(num, "is divisible by 3 only")
# elif num % 5 == 0:
#     print(num, "is divisible by 5 only")
# else:
#     print(num, "is not divisible by either 3 or 5")

# Print multiplication table for the number, skipping the multiplication by 3
# for i in range(1, 13):
#     if i == 3:
#         continue
#     print(num, "X", i, "=", num * i)



#Ask user to enter a password and check if it meets certain criteria (length, contains uppercase, lowercase, digit, special character)


#Ask user to enter a password and check if it is correct. If not, ask them to try again. Print account locked on 3 failed attempts.
password = str(input("Enter password: "))
if password == "Python123":
    print("Access granted")
else:
    attempts = 1
    while attempts < 3:
        password = str(input("Incorrect password. Please try again: "))
        if password == "Python123":
            print("Access granted")
            break
        attempts += 1
    else:
        print("Account locked due to too many failed attempts.")
        
# Prime numbers in a range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

#Tracing Nested Loops
for i in range(1, 5):
    for j in range(0, 4):
        if i == j:
            continue
        print(i, j)