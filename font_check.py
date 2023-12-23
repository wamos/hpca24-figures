import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Specify a font for the plot
font_path = "/Users/stingw/Downloads/calibri.ttf"  # Replace with the path to your desired font file
custom_font = fm.FontProperties(fname=font_path)
print(custom_font.get_name())
print(custom_font.get_family())

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting with the custom font
plt.plot(x, y)
plt.title('Plot with Custom Font', fontproperties=custom_font)
plt.xlabel('X-axis', fontproperties=custom_font)
plt.ylabel('Y-axis', fontproperties=custom_font)

plt.show()
