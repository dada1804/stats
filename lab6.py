import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read the dataset
data = pd.read_csv("student.csv")  # Replace "student_performance_dataset.csv" with the actual file name
# Analyze test scores in different subjects
subjects = ['math_score', 'science_score', 'english_score']  # Add more subjects if needed
for subject in subjects:
    subject_scores = data[subject]
    # Calculate descriptive statistics
    mean_score = np.mean(subject_scores)
    median_score = np.median(subject_scores)
    std_score = np.std(subject_scores)

    # Visualize the distribution using a box plot
    plt.boxplot(subject_scores)
    plt.xlabel(subject.capitalize() + " Score")
    plt.ylabel("Score")
    plt.title("Distribution of " + subject.capitalize() + " Scores")
    plt.show()

    # Print the results
    print(subject.capitalize() + " Scores:")
    print("Mean:", mean_score)
    print("Median:", median_score)
    print("Standard Deviation:", std_score)
    print()
