import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
from matplotlib.ticker import FuncFormatter

# Custom formatter function
def custom_formatter(value, pos):
    return f"{value:.1f}$\\times$"

# Data for four bars
categories = [" 1 app", "5 apps", "10 apps", "15 apps"]
values = [1.61, 1.29, 1.19, 1.11]

bar_width = 0.4  # Width of each bar

# Calculate bar positions
bar_positions = np.arange(len(categories))

# a dark blue for this
gray_shades = ['#2e2b5e', '#2e2b5e', '#2e2b5e', '#2e2b5e']

# Specify figsize in points
figsize_points = (250, 150)  # 450 points x 150 points

# Convert figsize from points to inches
figsize_inches = (figsize_points[0] / 72, figsize_points[1] / 72)

# Create a figure and axis
fig, ax = plt.subplots(figsize=figsize_inches)

# Specify a font for the plot
font_path = "/Users/stingw/Downloads/calibri.ttf"  # Replace with the path to your desired font file
custom_font = fm.FontProperties(fname=font_path)
font_size = '14'
#plt.margins(x=0.02)

# Create bar plots
bars = plt.bar(bar_positions, values, width=bar_width, color=gray_shades[2])

# Set ticks beneath each bar
tick_positions = [pos for pos in bar_positions]

y_ticks = np.arange(0, 2.1, 0.5)
plt.ylim(0,2.0)

plt.yticks(y_ticks, fontproperties=custom_font, fontsize=font_size)
# To adjust the boldness of the font, you can use the weight parameter 
# in the fontdict argument with a value other than 'bold'. 
# The weight parameter accepts values like 
# 'normal', 'bold', 'heavy', 'light', etc., or numerical values like 400, 700 
# for controlling the thickness of the font.
# plt.xticks(tick_positions, categories, fontdict={'weight': 'semibold'})
plt.xticks(tick_positions, categories, fontproperties=custom_font, fontsize=font_size)

# Add value labels vertically within each bar
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.2,
             f"{value:.1f}",
             ha='center',
             va='center',
             rotation='vertical',
             color='black', 
             fontsize=font_size,
             fontproperties=custom_font)

# Add grid below the bars (only horizontal grid with solid lines)
plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=1)

plt.tick_params(tick1On=False)
#plt.ylabel('Speedup/All-CPU', fontdict={'weight': 550})
plt.ylabel('Speedup \n Multi-Axl/All-CPU', fontproperties=custom_font, fontsize=font_size)

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

# Save the plot to a file (e.g., PNG format)
name = __file__.split("/")[-1]
name = name.split(".")[0]

name = "motivation-multiaxl-constraint"
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=1000)
plt.savefig(f'{name}.png', bbox_inches='tight', dpi=1000)

# Show the plot
plt.show()
