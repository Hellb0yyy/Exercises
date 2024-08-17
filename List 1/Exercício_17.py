def fibonacci(n):
    sequencia_fibonacci = [0, 1]
    while len(sequencia_fibonacci) < n:
        sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])
    return sequencia_fibonacci

primeiros_10_fibonacci = fibonacci(10)
print(primeiros_10_fibonacci)
