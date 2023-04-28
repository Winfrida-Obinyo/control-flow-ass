# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50.
def print_even_numbers():
    num = 0
    while num <= 50:
        if num % 2 == 0:
            num += 1
            continue
        print(num)
        num += 2 

# Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, and "Not 
# prime" if the number is not prime.
def check_prime(num):
    if num <= 1:
        print("Not prime")
    elif num == 2:
        print("Prime")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
            
# Write a function that takes a list of
# integers as input and prints the sum 
# of all the even numbers in the list.  
def sum_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    print(even_sum)
    
# Write a function that takes any two 
# integers as input, and prints the sum of all the 
def sum_divisible_by_3(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1  

    divisible_sum = 0
    for num in range(num1, num2+1):
        if num % 3 == 0:
            divisible_sum += num
    print(divisible_sum)         
            
            
            
    