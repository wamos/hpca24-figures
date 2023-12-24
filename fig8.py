import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm

# Custom formatter function
def custom_formatter(value, pos):
    return f"{int(value)}$\\%$"

# Sample data with 20 categories
categories = [f'Category {i+1}' for i in range(5)]
categories = ["Video\nSurvillence", "Sound\nDetetcion", "Brain\nStimulation", "Personal Info\nRedaction", "Database\nHash Join"]
value_labels = ["Retiring", "Bad Speculation", "Frontend Bound", "Backend Bound"]

# Modified large_array with 4 rows and 5 columns
large_array = np.array([[0.21, 0.19, 0.17, 0.22, 0.19],
       [0.12, 0.01, 0.02, 0.01, 0.03],
       [0.13, 0.05, 0.04, 0.07, 0.06],
       [0.54, 0.75, 0.77, 0.7 , 0.72]])

large_array = large_array * 100
values1 = large_array[0]
values2 = large_array[1]
values3 = large_array[2]
values4 = large_array[3]  # Added values for the fourth set

# Modified set of blue shades
blue_shades = ['#add8e6', '#3886e1', '#73b3ff', '#1c558e']
#blue_shades = ['#add8e6', '#1c558e', '#3886e1', '#46759b']


bar_width = 0.4  # Width of each bar

# Specify figure size in points
fig_size_pts = (500, 200)  # 500 points x 200 points

# Convert points to inches (1 inch = 72 points)
fig_size_inches = (fig_size_pts[0] / 72, fig_size_pts[1] / 72)

# Create bar plots with specified figure size and blue shades
fig, ax = plt.subplots(figsize=fig_size_inches)

# Specify a font for the plot
font_path = "/Users/stingw/Downloads/calibri.ttf"  # Replace with the path to your desired font file
custom_font = fm.FontProperties(fname=font_path)
font_size = '14'

# Reduce the white space between Y-axis and the 1st bar
#plt.margins(x=0.01)

# Plotting the first set of normalized values
bar1 = ax.bar(categories, values1, width=bar_width, label=value_labels[0], color=blue_shades[0], zorder=2)

# Plotting the second set of normalized values on top of the first one
bar2 = ax.bar(categories, values2, width=bar_width, bottom=values1, label=value_labels[1], color=blue_shades[1], zorder=2)

# Plotting the third set of normalized values on top of the previous ones
bar3 = ax.bar(categories, values3, width=bar_width, bottom=[v1 + v2 for v1, v2 in zip(values1, values2)], label=value_labels[2], color=blue_shades[2], zorder=2)

# Plotting the fourth set of normalized values on top of the previous ones
bar4 = ax.bar(categories, values4, width=bar_width, bottom=[v1 + v2 + v3 for v1, v2, v3 in zip(values1, values2, values3)], label=value_labels[3], color=blue_shades[3], zorder=2)

# Adding labels and title
ax.set_ylabel('Runtime Breakdown', fontproperties=custom_font, fontsize=font_size)
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20), fancybox=True, shadow=False, ncol=4, columnspacing=0.90, prop=custom_font)

# force to make the font larger
for text in legend.get_texts():
    text.set_fontsize(font_size)  # You can use other font size options or specify an integer value

plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=1)
plt.yticks(fontproperties=custom_font, fontsize=font_size)

# Tick position generation and adjustment
tick_loc = np.arange(len(categories))
ax.set_xticks(tick_loc)
ax.set_xticklabels(categories,fontproperties=custom_font, fontsize=font_size)

# Rotate x-axis labels for better readability
#ax.set_xticklabels(ticks, rotation=90, ha='right', va="center")

# Remove the visible ticks but keep the labels
ax.tick_params(tick1On=False)

# Remove the padding at the bottom of the figure
plt.subplots_adjust(bottom=0.1)

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

# Remove title for the figure
plt.title('')

name = __file__.split("/")[-1]
name = name.split(".")[0]
print(name)

name = "profiling_vtune"
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=600)
#plt.savefig(f'{name}.png', bbox_inches='tight', dpi=600)

# Display the plot
plt.show()
