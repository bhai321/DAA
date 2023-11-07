# Fibonacci without Recursion
def rec_fibo(n):
    if n<=1:
        return n
    else:
        return(rec_fibo(n-1) + rec_fibo(n-2))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_sequence = [0,1]
    for i in range(2,n+1):
        next_fib = fib_sequence[i - 1] + fib_sequence[i -2]
        fib_sequence.append(next_fib)

    return fib_sequence[n], len(fib_sequence) - 1

#nterm =10

nterm=int(input("Enter the number of fibonai series"))

if nterm<=0:
    print("Enter the positive integer")
else:
    print("Fabonaccii series with recursion")
    for i in range(nterm):
         print(rec_fibo(i), end=" ")

n = int(input("\n Enter the number: "))
fib_number , step_count = fibonacci(n)
print(f"Fabonacci({n}) = {fib_number}")
print(f"Number of steps taken: {step_count}")