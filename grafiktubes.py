import timeit
import random
import matplotlib.pyplot as plt 

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

x_size = []
y_robin = []
y_batman = []

for k in range (1, 100, 10):
    listr = [random.randint(1, 1000) for i in range(k * 100)]
    listb = listr.copy()

    timer = timeit.timeit(lambda: robin(listr), number = 10) / 10 
    #listb = [random.randint(1, 1000) for i in range(k * 100)]
    timeb = timeit.timeit(lambda: batman(listr), number = 10) / 10 

    print(f"Size: {k * 100}, Robin - Time: {timer}, "
          f"Batman: {batman(listb)}, Time: {timeb}")

    x_size.append(k * 100)
    y_robin.append(timer)
    y_batman.append(timeb)

plt.plot(x_size, y_robin, label = "Robin", marker = "o")
plt.plot(x_size, y_batman, label = "Batman", marker = "o")

plt.xlabel("Size")
plt.ylabel("Time")
plt.legend()
plt.show()

