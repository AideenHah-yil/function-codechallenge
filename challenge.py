def large_power(base, exponent):
    result = base ** exponent

    if result > 5000:
        return True
    else:
        return False

# Calling the large_power function and printing the results
print("Script started executing...")
print(large_power(10, 3))
print(large_power(2, 10))
print("Script finished executing.")

# Challenge 2
def divisible_by_ten(num):
    result = num % 10
    if result == 0:
        return True
    else:
        return False

# Calling the divisible_by_ten function and printing the results
print("Script started executing...")
print(divisible_by_ten(10))
print(divisible_by_ten(20))
print(divisible_by_ten(30))
print("Script finished executing.")
