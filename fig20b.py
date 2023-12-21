import matplotlib.pyplot as plt
import numpy as np

# Sample data with 8 categories
categories = [f'Category {i+1}' for i in range(8)]
ticks = ["1", "5", "10", "15"] * 2
value_labels = ["Kernel", "Data Restructuring", "Data Movement"]

large_array = np.array([[0.51408972, 0.37032805, 0.30759739, 0.22569554, 0.97252772,
        0.9591099 , 0.93927956, 0.93757771],
       [0.48278058, 0.60078151, 0.66653353, 0.75532336, 0.02155013,
        0.02125281, 0.02081339, 0.02077568],
       [0.0031297 , 0.02889044, 0.02586908, 0.0189811 , 0.00592215,
        0.01963729, 0.03990705, 0.04164661]])

values1 = large_array[0]
values2 = large_array[1]
values3 = large_array[2]

bar_width = 0.4  # Width of each bar

# Predefined list of blue shades
blue_shades = ['#a6cee3', '#2980b9', '#08306b']

# Specify figure size in points
fig_size_pts = (500, 200)  # 500 points x 200 points

# Convert points to inches (1 inch = 72 points)
fig_size_inches = (fig_size_pts[0] / 72, fig_size_pts[1] / 72)

# Create bar plots with specified figure size and blue shades
# plt.figure(figsize=fig_size_inches)

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=fig_size_inches)

# reduce the white space between Y-axis and the 1st bar
#plt.margins(x=0.01)

# Plotting the first set of normalized values
bar1 = ax.bar(categories, values1, width=bar_width, label=value_labels[0], color=blue_shades[0], zorder=2)

# Plotting the second set of normalized values on top of the first one
bar2 = ax.bar(categories, values2, width=bar_width, bottom=values1, label=value_labels[1], color=blue_shades[1], zorder=2)

# Plotting the third set of normalized values on top of the previous ones
bar3 = ax.bar(categories, values3, width=bar_width, bottom=[v1 + v2 for v1, v2 in zip(values1, values2)], label=value_labels[2], color=blue_shades[2], zorder=2)

# Adding vertical lines
for i in range(4, len(categories), 4):
    ax.axvline(x=i - 0.5, color='black', linestyle='--', linewidth=1)

# Adding labels and title
ax.set_ylabel('Runtime Breakdown')

# Adjust legend location to avoid extending outside the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, shadow=False, ncol=3)

plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=1)

# tick position generattion and adjustment
tick_loc = np.arange(len(categories))
tick_loc = tick_loc + 0.1
ax.set_xticks(tick_loc)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ticks, rotation=90, ha='right', va="center")

# remove the visible ticks but keep the labels
ax.tick_params(tick1On=False)

# Remove the padding at the bottom of the figure
plt.subplots_adjust(bottom=0.1)

group_labels = ["Multi-Axl", "DMX"]
# Add text labels for each group of four bars
for i in range(0, len(categories), 4):
    group_label = group_labels[i//4]
    group_center = (i + i + 3) / 2
    ax.text(group_center, -0.15, group_label, ha='center', va='center', color='black')

# Remove title for the figure
plt.title('')

name = "multi-kernel-breakdown"
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=1000)

# Display the plot
plt.show()
