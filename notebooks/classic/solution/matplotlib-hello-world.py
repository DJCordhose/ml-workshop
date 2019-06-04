# Create a scatter plot that has 4 data points
# * they shall be displayed as triangles
# * each point should have a different color
# * zoom into the plot so that you only see the two bottom left values

# plt.scatter?
# plt.colors?
# plt.xlim?
# plt.ylim?

plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], c=[1, 2, 3, 5], marker='^')
plt.xlim(0, 2)
plt.ylim(0, 15)