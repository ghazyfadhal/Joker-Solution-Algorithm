import timeit
import random

def robin(a):
    total = 0
    for i in range(0, len(a)):
        for j in range (i + 1, len(a)):
            if a[i] < a[j]:
                total += a[j]
                break
    return total

def batman(arr):
    n = len(arr)
    next_greater = [0] * n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            next_greater[idx] = arr[i]

        stack.append(i)

    result_sum = sum(next_greater) % 1000000001
    return result_sum

a = [random.randint(1, 100) for i in range(100)]

for i in range(0, 100):
    print("Data Array ke-", i + 1, ": ", a[i])

print()
print("Hasil Solusi Robin: ", robin(a))
print("Hasil Solusi Batman: ", batman(a))
