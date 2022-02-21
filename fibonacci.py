def fibonacci(n):
    sum_fibo = 0
    while n>0:
        sum_fibo = fibonacci(n-1)+fibonacci(n-2)
        n= n- 1
    return sum_fibo

number = int(input())
print(fibonacci(number))
