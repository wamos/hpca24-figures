import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm

# Custom formatter function
def custom_formatter(value, pos):
    return f"{int(value)}$\\%$"

# Sample data with 20 categories
categories = [f'Category {i+1}' for i in range(20)]
ticks = ["1", "5", "10", "15"] * 5
value_labels = ["Kernel", "Data Restructuring", "Data Movement"]

large_array = np.array([
        [0.78204543, 0.72678346, 0.65460248, 0.64359676, 0.70461316,
        0.56320458, 0.48889034, 0.41197378, 0.74318878, 0.62096363,
        0.49414883, 0.47736313, 0.7847989 , 0.72618979, 0.65039574,
        0.63891383, 0.70050496, 0.64468289, 0.57160187, 0.50044212],
        [0.16968719, 0.15769652, 0.14203478, 0.13964678, 0.13600598,
        0.10871099, 0.08278536, 0.07952009, 0.13186395, 0.11017755,
        0.0876768 , 0.08469853, 0.16396566, 0.15172064, 0.13588521,
        0.13348633, 0.25190912, 0.24131595, 0.22744762, 0.28532987],
        [0.04826738, 0.11552002, 0.20336274, 0.21675646, 0.15938086,
        0.32808443, 0.4283243 , 0.50850613, 0.12494727, 0.26885882,
        0.41817437, 0.43793834, 0.05123544, 0.12208957, 0.21371905,
        0.22759984, 0.04758592, 0.11400116, 0.20095051, 0.21422801]])

large_array = large_array * 100
values1 = large_array[0]
values2 = large_array[1]
values3 = large_array[2]

# Predefined list of blue shades
#blue_shades = ['#3498db', '#2980b9', '#1f618d', '#154360']
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

# reduce the white space between Y-axis and the 1st bar
plt.margins(x=0.01)

# Plotting the first set of normalized values
bar1 = ax.bar(categories, values1, label=value_labels[0], color=blue_shades[0], zorder=2)

# Plotting the second set of normalized values on top of the first one
bar2 = ax.bar(categories, values2, bottom=values1, label=value_labels[1], color=blue_shades[1], zorder=2)

# Plotting the third set of normalized values on top of the previous ones
bar3 = ax.bar(categories, values3, bottom=[v1 + v2 for v1, v2 in zip(values1, values2)], label=value_labels[2], color=blue_shades[2], zorder=2)

# Adding vertical lines
for i in range(4, len(categories), 4):
    ax.axvline(x=i - 0.5, color='black', linestyle='--', linewidth=1)

# Adding labels and title
ax.set_ylabel('Runtime Breakdown',fontproperties=custom_font)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, shadow=False, ncol=3,prop=custom_font)

plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=1)
plt.yticks(fontproperties=custom_font)

# tick position generattion and adjustment
tick_loc = np.arange(len(categories))
tick_loc = tick_loc + 0.25
ax.set_xticks(tick_loc)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ticks, rotation=90, ha='right', va="center", fontproperties=custom_font)

# remove the visible ticks but keep the labels
ax.tick_params(tick1On=False)

# Remove the padding at the bottom of the figure
plt.subplots_adjust(bottom=0.1)

# group_labels = ["Video\nSurvillence", "Sound\nDetetcion", "Brain\nStimulation", "Personal\nInfo Redaction", "Database\nHash Join"]
# # Add text labels for each group of four bars
# for i in range(0, len(categories), 4):
#     group_label = group_labels[i//4]
#     group_center = (i + i + 3) / 2
#     ax.text(group_center, -0.20, group_label, ha='center', va='center', color='black')

# Remove title for the figure
plt.title('')

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

name = __file__.split("/")[-1]
name = name.split(".")[0]
print(name)

name = "breakdown-dmx"

plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=1000)
plt.savefig(f'{name}.png', bbox_inches='tight', dpi=1000)

# Display the plot
plt.show()
