# -*- coding: utf-8 -*-
"""ShAI_BootCamp_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SP5Oco_w3N-CkQHjMdy_p17bDRWLqq1x

#About Dataset
salaries dataset generally provides information about the employees of an organization in relation to their compensation. It typically includes details such as how much each employee is paid (their salary), their job titles, the departments they work in, and possibly additional information like their level of experience, education, and employment history within the organization.

# Features
- 'Id'
- 'EmployeeName'
- 'JobTitle'
- 'BasePay'
- 'OvertimePay'
- 'OtherPay'
- 'Benefits'
- 'TotalPay' -> salary
- 'TotalPayBenefits'
- 'Year'
- 'Notes'
- 'Agency'
- 'Status'

# Tasks

1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.

2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.

3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.

4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.

5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.

6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.

8. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.

# Very Important Note
There is no fixed or singular solution for this assignment, so if anything is not clear, please do what you understand and provide an explanation.
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('/content/drive/ My Drive/SHAi/Salaries.csv')
df.head(125)

df.columns

"""# **Basic Data Exploration**"""

df.info()

columns_with_null = df.columns[df.isnull().any()]

print(columns_with_null)

"""# **Descriptive Statistics**"""

df.describe()

"""Salary statistics"""

#without benefits
print(" The statistics of salaries without benefits")
salary_statistics = df["TotalPay"].describe()
print(salary_statistics)
# with benefits
print(" The statistics of salaries with benefits")
salary_statistics_benefits = df["TotalPayBenefits"].describe()
print(salary_statistics_benefits)

"""# **Data Cleaning**

I choose to eliminate rows where 'BasePay' is null because, in most instances, employees are expected to have a basic salary, and it is common in real life .
"""

df = df.dropna(subset=['BasePay'])

"""I decide to substitute null values in ['OvertimePay', 'OtherPay', 'Benefits'] with zero, as these components are not consistently applicable to all employees; some may not have received additional payments and benefits beyond their basic salary."""

columns_to_replace = ['OvertimePay', 'OtherPay', 'Benefits']
df[columns_to_replace] = df[columns_to_replace].fillna(0)

"""
Substitute null values in 'Notes' and 'Status' with zero, as every instance contains null values in these columns."""

columns_to_replace2 = ['Notes', 'Status']
df[columns_to_replace2] = df[columns_to_replace2].fillna(0)

"""
Ensure that there are no remain null values."""

columns_with_null = df.columns[df.isnull().any()]
print(columns_with_null)

"""# **Basic Data Visualization**

Create histogram
"""

import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Year', y='TotalPay', ci=None, palette='Greens')
plt.title('Distribution of Salaries Over the Years')
plt.xlabel('Year')
plt.ylabel('TotalPay')

plt.show()

"""**There is no Depertment column for each employee, so we cannot draw this pie chart**

# Set the style for Seaborn
sns.set(style="whitegrid")

# Calculate the proportion of employees in each department
department_counts = df['Depertment'].value_counts()

# Create a pie chart with multiple colors using Matplotlib
plt.figure(figsize=(8, 8))
colors = sns.color_palette("pastel", len(department_counts))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Proportion of Employees in Different Departments')
plt.show()

# Good Luck!

# **Grouped Analysis**
"""

# Create a new column indicating whether an individual has overtime or not
df['Has_Over_time'] = df['OvertimePay'] > 0
average_salary_with_overtime = df.groupby('Has_Over_time')['BasePay'].mean()
print("average_salary_with_overtime:",average_salary_with_overtime)

# Group the data by 'Year' and calculate the average 'TotalPayBenefits' for each year
average_salary_by_year = df.groupby('Year')['TotalPayBenefits'].mean()
print(average_salary_by_year)

"""# **Simple Correlation Analysis:**"""

# Calculate the correlation coefficient between 'BasePay' and 'Benefits'
correlation = df['BasePay'].corr(df['Benefits'])


print(f"Correlation between 'BasePay' and 'Benefits': {correlation}")

# Create a scatter plot to visualize the relationship
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='BasePay', y='Benefits')
plt.title('Scatter Plot: Base Pay vs Benefits')
plt.xlabel('Base Pay')
plt.ylabel('Benefits')
plt.show()

sns.set(style="whitegrid")

correlation2 = df['BasePay'].corr(df['OvertimePay'])

# Print the correlation coefficient
print(f"Correlation between 'BasePay' and 'OvertimePay': {correlation2 }")

# Create a scatter plot for 'BasePay' vs 'Benefits' with blue color
plt.figure(figsize=(20, 16))
sns.scatterplot(data=df, x='BasePay', y='Benefits', label='Base Pay vs Benefits', color='blue')

# Create a scatter plot for 'BasePay' vs 'OvertimePay' with orange color
sns.scatterplot(data=df, x='BasePay', y='OvertimePay', label='Base Pay vs Overtime Pay', color='red')

plt.legend()

plt.title('Scatter Plots: Base Pay vs Benefits and Overtime Pay')
plt.xlabel('Base Pay')
plt.show()

"""# **Summary of Insights**

**Dataset Notes:**
Upon analyzing the dataset, it was observed that there is no 'Department' column for each employee, making it challenging to associate employees with specific departments. It is recommended to include a 'Department' column to enhance the granularity of the analysis. Additionally, ensuring that each column accurately described  would contribute to  more comprehensive analysis. Including the currency is crucial for the interpretation and clarity of the reported values.

**Negative Payment Values:**
Investigation into the negative values in the Payments to Employee columns revealed that they could be attributed to data entry errors, refunds, or deductions. Further examination of these records is necessary to determine the root cause and address any anomalies in the dataset.

**Analysis of Total Pay with Benefits:**
The analysis of 'Total Pay with Benefits' revealed key insights. The mean value of Total Pay with Benefits is 93,692.55, with a standard deviation of 62,793.53, indicating how much your salaries typically differ from their mean. The maximum salary is 567,595.43, while the minimum salary is -618.13. The yearly breakdown of Total Pay with Benefits showed an increase from 2011 to 2013, with 2013 having the highest average, followed by a slight decrease in 2014. Notably, the total payment in 2011 is comparatively low with 71744.103871.

**Correlation Analysis:**
An investigation into the correlation between 'BasePay' and other variables was conducted. The correlation between 'BasePay' and 'Benefits' was found to be 0.65, indicating a moderate positive correlation. This suggests that an increase in base pay tends to positively affect benefits. On the other hand, the correlation between 'BasePay' and 'OvertimePay' was 0.27, indicating a weaker correlation. It implies that overtime pay does not have a substantial relation to the increase or decrease of base salary.
"""