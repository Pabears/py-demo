import time

import matplotlib.pyplot as plt

# plt.figure('lalala')
plt.title('gagaga')
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.ylim(0, 10000)
l1 = []
l2 = []
s = []
i = 0
while i < 20:
    s.append(i)
    l1.append(2 ** i)
    l2.append(100 * i)
    i += 1
plt.plot(s, l1, label='2 ** i')
plt.plot(s, l2, label='100 * i')
plt.legend()
plt.show()
