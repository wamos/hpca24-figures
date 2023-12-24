import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm

# Custom formatter function
def custom_formatter(value, pos):
    return f"{value:.1f}$\\times$"

# New data for six ticks and four categories, each with 6 bars
#ticks = ["tick A", "tick B", "tick C", "tick D", "tick E", "tick F"]
ticks = ["Video\nSurvillence", "Sound\nDetetcion", "Brain\nStimulation", "Personal Info\nRedaction", "Database\nHash Join", "GeoMean"]
values1 = [5.1,  2.5,  2.0,  1.5,  7.0,  3.0]
values2 = [10.2, 6.8,  5.6,  2.7, 12.7,  6.6]
values3 = [10.9, 11.3, 11.2, 4.3, 18.0, 10.1]
values4 = [15.3, 13.4, 13.0, 7.8, 22.8, 13.6]
labels = [" 1 app", "5 apps", "10 apps", "15 apps"]

num_bar_per_group = 4
bar_width = 0.12  # Width of each bar

# Calculate bar positions
bar_positions1 = np.arange(len(values1))
# make the bar closer
# this makes sure the space between bars is exactly 1 bar width
bar_positions1 = 0.01 + bar_positions1 * bar_width * (num_bar_per_group + 1)
bar_positions2 = [pos + bar_width for pos in bar_positions1]
bar_positions3 = [pos + bar_width for pos in bar_positions2]
bar_positions4 = [pos + bar_width for pos in bar_positions3]

# Calculate the center position for each group of bars
bar_centers = [(pos1 + pos4) / 2 for pos1, pos4 in zip(bar_positions1, bar_positions4)]

# Predefined list of blue shades
#blue_shades = ['#3498db', '#2980b9', '#1f618d', '#154360']
blue_shades = ['#add8e6', '#73b3ff', '#3886e1', '#1c558e']

# Specify figure size in points
fig_size_pts = (500, 200)  # 600 points x 200 points

# Convert points to inches (1 inch = 72 points)
fig_size_inches = (fig_size_pts[0] / 72, fig_size_pts[1] / 72)

# Create bar plots with specified figure size and blue shades
plt.figure(figsize=fig_size_inches)

y_ticks = np.arange(0, 29, 4)
plt.ylim(0, )

# Specify a font for the plot
font_path = "/Users/stingw/Downloads/calibri.ttf"  # Replace with the path to your desired font file
custom_font = fm.FontProperties(fname=font_path)
font_size = '14'

# reduce the white space between Y-axis and the 1st bar
plt.margins(x=0.01)

# Plot bars with zorder to ensure they are below grid lines
bars1 = plt.bar(bar_positions1, values1, width=bar_width, label=labels[0], color=blue_shades[0], zorder=2)
bars2 = plt.bar(bar_positions2, values2, width=bar_width, label=labels[1], color=blue_shades[1], zorder=2)
bars3 = plt.bar(bar_positions3, values3, width=bar_width, label=labels[2], color=blue_shades[2], zorder=2)
bars4 = plt.bar(bar_positions4, values4, width=bar_width, label=labels[3], color=blue_shades[3], zorder=2)

# Add value labels on top of each bar, except bars1
for bar, values in zip([bars1, bars2, bars3, bars4], [values1, values2, values3, values4]):
    for value, position in zip(values, bar):
        plt.text(position.get_x() + position.get_width() / 2 + 0.005,
                 position.get_height() + 0.25,
                 str(value),
                 ha='center',
                 va='bottom',
                 rotation='vertical',
                 fontsize=font_size,  
                 fontproperties=custom_font,
                 color='black')

# Remove title for the figure
plt.title('')

# Add grid below the bars
plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=1)

# Set x-axis ticks and labels at the center of each group of bars
plt.xticks(bar_centers, ticks, fontproperties=custom_font,  fontsize="12")
plt.tick_params(tick1On=False)
plt.yticks(y_ticks, fontproperties=custom_font, fontsize=font_size)
plt.ylabel('Throughput Improvement\nDMX/Multi-Axl', fontproperties=custom_font,  fontsize=font_size)

# Add legend outside and on top of the figure with no shadow
legend =  plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.20), fancybox=True, shadow=False, ncol=4, prop=custom_font)

# force to make the font larger
for text in legend.get_texts():
    text.set_fontsize(font_size)  # You can use other font size options or specify an integer value

name = __file__.split("/")[-1]
name = name.split(".")[0]
print(name)
name = "throughput-improvement"

# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))

# Save the plot to a file (e.g., PNG) with the updated file name
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=600)

# Show the plot
plt.show()
