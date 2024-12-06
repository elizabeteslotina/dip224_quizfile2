from openpyxl import Workbook, load_workbook
import pandas as pd
file_path = "EmployeeData.xlsx"
data = pd.read_excel(file_path)

#1
it_employee = data[data['Department'] == 'IT']
it_employee_count = len(it_employee)
print(it_employee_count)

#2
employee = data[data['Department'] == 'Accounting']
max_age = employee['Age'].max()
print(max_age)

#3
employee = data[data['Department'] == 'Finance']
average_age = employee['Age'].mean()
average_age = round(average_age)
print(average_age)

#4
employee=data[(data['Annual Salary'] > 100000)&(data['Annual Salary'] < 250000)]
count= employee.shape[0]
print(count)

#5
max_alga= data[data['Annual Salary'] == data['Annual Salary'].max()]
vecums= max_alga['Age'].values[0]
print(vecums)