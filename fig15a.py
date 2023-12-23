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

large_array = np.array([[0.28696495, 0.16041532, 0.12695349, 0.10568781, 0.18560204,
        0.06440024, 0.03920463, 0.02852659, 0.24557641, 0.07831134,
        0.05093976, 0.03870384, 0.16265031, 0.12394444, 0.12394444,
        0.10513596, 0.19958095, 0.09812168, 0.06912248, 0.05317379],
       [0.61857791, 0.47484673, 0.54260399, 0.61922132, 0.65716622,
        0.55874815, 0.69817022, 0.78037861, 0.53423314, 0.43666196,
        0.58788827, 0.68687905, 0.79651028, 0.62996818, 0.65138709,
        0.68612025, 0.7371472 , 0.6870053 , 0.75759597, 0.81352607],
       [0.09445714, 0.36473795, 0.33044252, 0.27509087, 0.15723174,
        0.37685161, 0.26262515, 0.1910948 , 0.22019045, 0.4850267 ,
        0.36117197, 0.27441711, 0.04083941, 0.24608738, 0.22466847,
        0.20874379, 0.06327185, 0.21487302, 0.17328155, 0.13330014]])

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
ax.set_ylabel('Runtime Breakdown', fontproperties=custom_font)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, shadow=False, ncol=3, prop=custom_font)

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

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

# group_labels = ["Video\nSurvillence", "Sound\nDetetcion", "Brain\nStimulation", "Personal\nInfo Redaction", "Database\nHash Join"]
# # Add text labels for each group of four bars
# for i in range(0, len(categories), 4):
#     group_label = group_labels[i//4]
#     group_center = (i + i + 3) / 2
#     ax.text(group_center, -0.20, group_label, ha='center', va='center', color='black')

# Remove title for the figure
plt.title('')

name = __file__.split("/")[-1]
name = name.split(".")[0]
print(name)

name = "breakdown-multiaxl"
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=1000)
plt.savefig(f'{name}.png', bbox_inches='tight', dpi=1000)

# Display the plot
plt.show()
