from math import factorial, pow, pi, sqrt, exp
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

q = 0.4
p = 0.6
n = 10
k = 0
list1 = []
list2 = []
while k <= n:
    temp = (factorial(n) / (factorial(n - k) * factorial(k))) * pow(p, k) * pow(q, n - k)
    temp2 = (1 / sqrt(2 * pi * n * p * q)) * exp(-(pow(k - n * p, 2) / (2 * n * p * q)))
    list1.append(temp)
    list2.append(temp2)
    k += 1
for i in list1:
    print(i)
print("----------------------------------------------------------")
for i in list2:
    print(i)
fig, ax, = plt.subplots()
ax.plot(list1, marker='.', linewidth=1)
ax.plot(list2, marker='.', linewidth=1, color="orange")
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.grid(True)
fig.savefig('мой график.png', quality=100)
