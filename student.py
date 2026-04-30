import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Generate Student Data
# -------------------------------
np.random.seed(0)

students = ['Student_' + str(i) for i in range(1, 21)]

data = {
    'Name': students,
    'Math': np.random.randint(40, 100, 20),
    'Science': np.random.randint(40, 100, 20),
    'English': np.random.randint(40, 100, 20),
    'Computer': np.random.randint(40, 100, 20)
}

df = pd.DataFrame(data)

# -------------------------------
# Step 2: Add Total & Average
# -------------------------------
df['Total'] = df.iloc[:, 1:5].sum(axis=1)
df['Average'] = df.iloc[:, 1:5].mean(axis=1)

# -------------------------------
# Step 3: Statistical Analysis
# -------------------------------
print("\n--- Statistical Analysis ---")
print(df.describe())

# Mean, Median, Std Dev
print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))

# -------------------------------
# Step 4: Identify Performers
# -------------------------------
topper = df.loc[df['Total'].idxmax()]
low_performer = df.loc[df['Total'].idxmin()]

print("\nTopper:\n", topper)
print("\nLow Performer:\n", low_performer)

# -------------------------------
# Step 5: Subject-wise Comparison
# -------------------------------
subject_means = df.iloc[:, 1:5].mean()
print("\nSubject-wise Average:\n", subject_means)

# -------------------------------
# Step 6: Visualization
# -------------------------------

# 1. Bar Graph (Subject Averages)
subject_means.plot(kind='bar', title='Average Marks per Subject')
plt.ylabel('Marks')
plt.show()

# 2. Line Plot (Student Performance)
df.set_index('Name')[['Math','Science','English','Computer']].plot()
plt.title('Student-wise Performance')
plt.ylabel('Marks')
plt.show()

# 3. Histogram (Total Marks)
df['Total'].plot(kind='hist', bins=10)
plt.title('Distribution of Total Marks')
plt.xlabel('Total Marks')
plt.show()

# 4. Pie Chart (Subject Contribution for Topper)
topper_subjects = topper[['Math','Science','English','Computer']]
topper_subjects.plot(kind='pie', autopct='%1.1f%%', title='Topper Subject Contribution')
plt.ylabel('')
plt.show()
