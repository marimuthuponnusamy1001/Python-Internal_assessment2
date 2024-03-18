# -*- coding: utf-8 -*-
"""LVADSUSR98-Marimuthu_P-IA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11CmrtcdBu0MOqlUiaOrl0lCWR9hpqVEK
"""

import numpy as np
def rgb_to_grays(rgb_image):
  grayscale = np.dot(rgb_image, [0.2989, 0.5870, 0.1140])
  return grayscale

rgb_image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                       [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                       [[127, 127, 127], [200, 200, 200], [50, 50, 50]]])

grayscale = rgb_to_grays(rgb_image)
print(grayscale)



import numpy as np

def n_data(data):
  n_data = data - np.mean(data, axis=0)
  n_data = n_data / np.std(data, axis=0)

  return n_data

data = np.array([[100, 70, 70],
                  [170, 60, 66],
                  [630, 90, 99]])

n_data = n_data(data)

print(n_data)



import numpy as np
sensor_data = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]]])
print(sensor_data.shape)
flat_data = sensor_data.reshape(sensor_data.shape[1], -1)
print(flat_data)
reshape_data = flat_data.reshape(-1, flat_data.shape[1] // sensor_data.shape[2])
print(reshape_data)



import numpy as np
ath_data = np.array([
    [10, 12, 15, 18],
    [14, 15, 13, 16],
    [8, 9, 11, 14]])
value = ath_data[:,-1] - ath_data[:,0]
print(value)



import numpy as np

def  avg_score(scores):
  n_students, n_subjects, _ = scores.shape
  valid_mark = scores != -1
  last_subjects = scores[:, -min(3, n_subjects):, :]
  valid_last_subjects = last_subjects[valid_mark[:, -min(3, n_subjects):, :]]
  avg_scores = np.mean(valid_last_subjects, axis=1)
  return avg_scores

scores = np.array([
  [[70, 80, 90], [85, 90, 95], [-1, 100, 98]],
  [[60, 75, 85], [90, 80, 75], [88, 92, 95]]])

avg = avg_score(scores)
print(avg)



import numpy as np

def adjust_temp(temp, arr):

  return temp + arr[:, np.newaxis]

temp = np.array([
  [10.5, 12.3, 14.7, 15.9, 17.8, 18.9, 20.3, 19.7, 17.2, 14.1, 11.3, 9.4],
  [12.1, 13.8, 15.9, 17.5, 19.1, 20.4, 21.8, 21.1, 18.6, 15.4, 12.7, 10.9],
])

arr = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3])
arr = arr.reshape(1,12)
adjusted_temp = adjust_temp(temp, arr)
print(adjusted_temp)



import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami',
                 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}
fil_data = [employee for employee in data.values() if employee['Age'] < 45 and 'HR' not in employee['Department']]
fil_data = [{'Name': employee['Name'], 'City': employee['City']} for employee in fil_data]
print(fil_data)



import pandas as pd
data = {
    "Product": ["Apples", "Bananas", "Cherries", "Dates", "Elderberries", "Flour", "Grapes"],
    "Category": ["Fruit", "Fruit", "Fruit", "Fruit", "Fruit", "Bakery", "Fruit"],
    "Price": [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    "Promotion": [True, False, True, True, False, True, False]
}

df = pd.DataFrame(data)
products = df[(df["Category"] == "Fruit") & (df["Price"] > df["Price"].mean()) & (~df["Promotion"])]
promotions = products["Product"].tolist()
print(promotions)



import pandas as pd
employee = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Department": ["HR", "IT", "Finance", "IT", "Marketing"],
    "Manager": ["John", "Rachel", "Emily", "Rachel", "Mike"]})

project = pd.DataFrame({
    "Employee": ["Alice", "Charlie", "Eve", "David"],
    "Project": ["P1", "P3", "P2", "P4"]})
df = pd.merge(employee, project, on='Employee')
print(df[['Project', 'Department', 'Manager']])



import pandas as pd
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}
df = pd.DataFrame(data)
avg_sales = df.groupby('Department')['Sales'].mean()
print(avg_sales)