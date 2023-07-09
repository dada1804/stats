import numpy as np
from scipy.stats import spearmanr
import seaborn as sns
import matplotlib.pyplot as plt

# SMIP and DBMS scores
SMIP = [70, 46, 94, 34, 20, 86, 18, 12, 56, 64, 42]
DBMS = [60, 66, 90, 46, 16, 98, 24, 8, 32, 54, 62]

# Compute Spearman rank correlation coefficient
corr_coeff, p_value = spearmanr(SMIP, DBMS)

# Interpret the results
if p_value < 0.05:
    interpretation = "There is a significant Spearman rank correlation."
else:
    interpretation = "There is no significant Spearman rank correlation."

print("Spearman rank correlation coefficient:", corr_coeff)
print("p-value:", p_value)
print(interpretation)

# Create a correlation matrix
correlation_matrix = np.corrcoef(SMIP, DBMS)

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True)
plt.xlabel('DBMS')
plt.ylabel('SMIP')
plt.title('Spearman Rank Correlation Heatmap')
plt.show()

#Create a histogram
plt.hist(correlation_matrix)
plt.title("Histogram")
plt.xlabel('DBMS')
plt.ylabel('SMIP')
plt.show()
