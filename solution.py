import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problem 1

x = np.arange(0, 20)
y = ((-3 / 4) * x) + (29 / 4)

plt.figure()

point1 = [3, 7]
point2 = [5, 2]

# Defining values for y using the equation of a line (y = mx + c)

plt.grid(True)
plt.plot(x, y, "k-")
plt.scatter(point1, point2, c = "#3d3d3dcc", s = 100)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, 10)
plt.ylim(0, 10)

# fig, ax = plt.subplots(1, 2, figsize = (5, 5))
# ax = ax.flatten()

# x = np.arange(0, 20)
# y = ((-3 / 4) * x) + (29 / 4)
# z = np.zeros(20) + 3

# point1 = [3, 7]
# point2 = [5, 2]

# point3 = [1, 4]
# point4 = [1, 4]

# ax[0].grid(True)
# ax[0].plot(x, y, "k-")
# ax[0].scatter(point1, point2, c = "#3d3d3d3d", s = 100)
# ax[0].set_xlabel("x")
# ax[0].set_ylabel("y")
# ax[0].set_xlim(0, 10)
# ax[0].set_ylim(0, 10)

# ax[1].grid(True)
# ax[1].plot(z, x, "k-")
# ax[1].scatter(point3, point4, s = 100)
# ax[1].set_xlim(0, 10)
# ax[1].set_ylim(0, 10)

# fig, ax = plt.subplots(figsize = (8, 5))

# x = np.linspace(0, 10, 50)
# y = np.sin(np.cos(x) ** 2)

# ax.plot(x, y, "k-")
# ax.set_ylim(0, 1)

# plt.show()


# Problem 2

data = pd.read_parquet("https://star.herts.ac.uk/~kuhn/DHV/exercises_problem2.parquet")

print(data.head)

data.set_option("display.max_rows", None)

# x = [data.var1, data.var2, data.var3]
# y = [data.index, data.index, data.index, data.var2, data.var1, data.var1, data.var3, data.var3, data.var2]


# for i, var in enumerate(x):
#     for j in y:
#         print(var, j)

plt.show()
