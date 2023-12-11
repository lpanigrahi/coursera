
def fibonacci(n):
    fib_series = [0, 1]  # Initialize the series with the first two numbers
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]  # Calculate the next number
        fib_series.append(next_num)  # Add the next number to the series
    return fib_series


# Test the function
n = 10  # Number of Fibonacci numbers to generate
fib_nums = fibonacci(n)
print(fib_nums)
