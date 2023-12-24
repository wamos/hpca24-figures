import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties

# Custom formatter function
def custom_formatter(value, pos):
    return f"{int(value)}$\\%$"

# Sample data with 8 categories
categories = [f'Category {i+1}' for i in range(8)]
ticks = ["All-CPU", "Multi-Axl"] * 4
value_labels = ["Kernel", "Data Restructuring", "Data Movement"]

large_array = np.array([[0.82602185, 0.21163839, 0.53141449, 0.09967586, 0.39124551,
        0.07368465, 0.3025162 , 0.05792893],
       [0.17397815, 0.69167359, 0.46858551, 0.57714922, 0.60875449,
        0.66492584, 0.6974838 , 0.73279668],
       [0.        , 0.09668803, 0.        , 0.32317491, 0.        ,
        0.2613895 , 0.        , 0.20927439]])

large_array = large_array * 100
values1 = large_array[0]
values2 = large_array[1]
values3 = large_array[2]

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

# Specify a font for the plot
font_path = "/Users/stingw/Downloads/calibri.ttf"  # Replace with the path to your desired font file
custom_font = fm.FontProperties(fname=font_path)
font_size = '14'

# reduce the white space between Y-axis and the 1st bar
# plt.margins(x=0.01)

bar_width = 0.4  # Width of each bar

# Plotting the first set of normalized values
bar1 = ax.bar(categories, values1, width=bar_width, label=value_labels[0], color=blue_shades[0], zorder=2)

# Plotting the second set of normalized values on top of the first one
bar2 = ax.bar(categories, values2, width=bar_width, bottom=values1, label=value_labels[1], color=blue_shades[1], zorder=2)

# Plotting the third set of normalized values on top of the previous ones
bar3 = ax.bar(categories, values3, width=bar_width, bottom=[v1 + v2 for v1, v2 in zip(values1, values2)], label=value_labels[2], color=blue_shades[2], zorder=2)

# Adding vertical lines
for i in range(2, len(categories), 2):
    ax.axvline(x=i - 0.5, color='black', linestyle='--', linewidth=1)

# Adding labels and title
ax.set_ylabel('Runtime Breakdown', fontproperties=custom_font, fontsize=font_size)

# Adjust legend location to avoid extending outside the plot
# Create a FontProperties object with the desired font size
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20), fancybox=True, ncol=3, prop=custom_font)

# force to make the font larger
for text in legend.get_texts():
    text.set_fontsize(font_size)  # You can use other font size options or specify an integer value

plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=1)

plt.yticks(fontproperties=custom_font, fontsize=font_size)
# tick position generattion and adjustment
# Calculate the bar positions
bar_positions = np.arange(len(categories))

# Set the tick positions to the center of each bar
tick_positions = 0.15 + bar_positions + bar_width / 2 
ax.set_xticks(tick_positions)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ticks, ha='right', va="center", fontproperties=custom_font, fontsize="12")

# remove the visible ticks but keep the labels
ax.tick_params(tick1On=False)

# Remove the padding at the bottom of the figure
plt.subplots_adjust(bottom=0.1)

# group_labels = [" 1 app", "5 apps", "10 apps", "15 apps"]
# # Add text labels for each group of four bars
# for i in range(0, len(categories),2):
#     group_label = group_labels[i//2]
#     group_center = (i + i + 1) / 2
#     ax.text(group_center, -0.15, group_label, ha='center', va='center', color='black')

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

# Remove title for the figure
plt.title('')

name = "motivation-multiaxl-breakdown"

plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=1000)
plt.savefig(f'{name}.png', bbox_inches='tight', dpi=1000)

# Display the plot
plt.show()
