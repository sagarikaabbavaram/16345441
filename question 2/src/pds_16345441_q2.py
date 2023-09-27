# -*- coding: utf-8 -*-
"""pds_16345441_q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v4dqE2P31Gx7cGvdw75A8bBYMDgByQCv

DATA VISUALISATION 1
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

# Load the data
data = pd.read_csv('StudentsPerformance.csv')
data
data.to_csv('cleaned_Data2.csv', index=False)

# Generate a direct download link
from google.colab import files
files.download('cleaned_Data2.csv')

"""histplot between input data and gender"""

plt.plot()
ax =sb.histplot(data, x = 'gender', color='black')

"""Based on the information provided above, we can conclude that the data is not skewed or biased in terms of gender, as it contains a nearly equal number of samples for both males and females."""

plt.plot()
ax =sb.histplot(data, x = 'race/ethnicity', color='black')

plt.plot()
ax =sb.histplot(data, x = 'lunch', color='black')

plt.plot()
ax =sb.histplot(data, x = 'parental level of education', color='black')

"""DATA VISUALISATION 2

barplot of race/ethnicity and math score amonge gender
"""

sb.barplot(data=data,x='race/ethnicity',y='math score',hue='gender')

"""The plot above illustrates the relationship between race/ethnicity and the average math scores, stratified by gender. From this graph, we can deduce that males consistently achieve significantly higher average math scores than females, regardless of their ethnicity. However, it's worth noting that for both males and females, individuals in group E tend to attain higher math averages compared to all other ethnicities."""



"""This visualization shows the correlation coefficients between all of the student variables in the dataset. It can be used to identify which variables are strongly correlated with each other.

DATA VISUALISATION 3
"""

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Create the heatmap
plt.figure()
sb.heatmap(correlation_matrix, annot=True)
plt.title('Heatmap of correlation coefficients between student variables')
plt.show()

"""This visualization displays the correlation coefficients among all the student variables within the dataset. It serves as a tool for pinpointing which variables exhibit strong correlations with one another. This graphic simplifies the process of recognizing the robust associations between different student variables. For instance, if the heatmap reveals a significant correlation between student grades and attendance, it suggests that attendance plays a crucial role in determining student success.

violinplot of parental level of education and writing score among gender

DATA VISUALISATION 4
"""

sb.violinplot(data,x="parental level of education",y="writing score",hue='gender', split=True)

"""Based on the provided figure, it can be observed that, among students with parents holding master's degrees, males tend to achieve slightly higher average scores compared to females, especially when compared to students with parents holding other qualifications. However, in a general sense, females tend to outperform males regardless of their parents' educational backgrounds. It's also evident that students with parents who have master's degrees generally perform well academically, but the reverse may not necessarily hold true."""



"""catplot of reading score and gender for the different test preparation course

DATA VISUALISATION 5
"""

sb.catplot(data=data,x='gender',y='reading score',kind='box',col='test preparation course', whis=[0,100])
plt.show()

"""From the provided data, it's evident that students who have completed the course tend to achieve higher average scores in reading compared to students who haven't completed the course or haven't taken any course, regardless of their gender. Moreover, it's noteworthy that, in general, female students tend to score higher in reading compared to their male counterparts. However, this trend is the opposite when it comes to math scores."""