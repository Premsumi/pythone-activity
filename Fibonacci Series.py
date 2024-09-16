def fibonacci_series(n):
    # Initialize the first two terms
    a, b = 0, 1
    
    # Print the first term
    if n > 0:
        print(a, end=' ')
        
    # Print the rest of the terms
    for _ in range(1, n):
        print(b, end=' ')
        a, b = b, a + b

# Get the number of terms from the user
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_series(num_terms)
except ValueError:
    print("Invalid input. Please enter an integer.")
