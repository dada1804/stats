 import numpy as np
import matplotlib.pyplot as plt

# Heights data
heights = [165, 170, 168, 172, 175, 169, 180, 160, 165, 172, 168, 176, 170, 173, 165]

mean_height = np.mean(heights)
print("Mean Height:", mean_height)

median_height = np.median(heights)
print("Median Height:", median_height)

mode_height = np.argmax(np.bincount(heights))
print("Mode Height:", mode_height)

std_h = np.std(heights)
print("Standard Deviation:", std_h)

plt.hist(heights, bins=5, edgecolor='black')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.title('Distribution of Heights')
plt.show()
