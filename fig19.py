import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm

# Custom formatter function
def custom_formatter(value, pos):
    return f"{value:.1f}$\\times$"

labels = [" 1 app", "5 apps", "10 apps", "15 apps"]
categories = ['Over-provision', 'Under-provision']
values = np.array([[3.5, 3.3],  # Values for Category A
                   [3.9, 3.4],  # Values for Category B
                   [5.4, 4.5],  # Values for Category C
                   [6.5, 5.1]]) # Values for Category D

# Specify figsize in points
figsize_points = (600, 200)  # 450 points x 150 points

# Convert figsize from points to inches
figsize_inches = (figsize_points[0] / 72, figsize_points[1] / 72)

# Create a figure and axis
fig, ax = plt.subplots(figsize=figsize_inches)

# Specify a font for the plot
font_path = "/Users/stingw/Downloads/calibri.ttf"  # Replace with the path to your desired font file
custom_font = fm.FontProperties(fname=font_path)

# Define different shades of blue
#blue_shades = ['#3498db', '#2980b9', '#1f618d', '#154360']
blue_shades = ['#add8e6', '#73b3ff', '#3886e1', '#1c558e']

bar_width = 0.2  # Adjust the width of each bar

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Set the grid lines behind the bars
ax.set_axisbelow(True)

# Create a grouped bar plot with different shades of blue
bar_width = 0.2  # Adjust the width of each bar
bar_positions = np.arange(len(categories)) * (len(values) + 1) * bar_width

for i in range(len(values)):
    bars = ax.bar(bar_positions + i * bar_width, values[i], width=bar_width, label=f'{labels[i]}', color=blue_shades[i])

    # Add vertical value labels on top of each bar
    for bar, value in zip(bars, values[i]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.15, str(value),
                ha='center', va='top', color='white', rotation='vertical', fontproperties=custom_font)

# Set the x-axis ticks in the middle of each group
#ax.set_xticklabels(categories)
#ax.set_xticks(bar_positions + (len(values) - 1) * bar_width / 2)
#plt.xticks(bar_positions + (len(values) - 1) * bar_width / 2, categories, fontdict={'weight': 'semibold'})
plt.xticks(bar_positions + (len(values) - 1) * bar_width / 2, categories, fontproperties=custom_font)
plt.yticks(fontproperties=custom_font)

plt.tick_params(tick1On=False)
#plt.ylabel('Speedup/Multi-Axl', fontdict={'weight': 'semibold'})
plt.ylabel('Speedup DMX/Multi-Axl', fontproperties=custom_font)

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

# Add legend above the figure, aligned with the center line
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.01), fancybox=True, shadow=False, ncol=4)
#legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.155), fancybox=True, shadow=False, ncol=4, prop={'weight': 'semibold'})
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.155), fancybox=True, shadow=False, ncol=4, prop=custom_font)

# Calculate the legend width in inches
legend_width_inches = legend.get_bbox_to_anchor().width

# Adjust the legend position to center it
legend.set_bbox_to_anchor((0.5 - legend_width_inches / 2, 1.155))

# Save the plot to a file (e.g., PDF format)
name = __file__.split("/")[-1]
name = name.split(".")[0]

name = "standalone-underprovision"
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=1000)

# Show the plot
plt.show()
