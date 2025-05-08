import pandas as pd
#reading the csv file
df=pd.read_csv('employees.csv')

#initial inspection
print("DATA")
print(df) #printing the data
print("Head:\n",df.head()) #first five rows
print("tail:\n",df.tail()) #last five rows
print("Summary:\n",df.info()) #summary
print("Descriptive data:\n",df.describe()) #descriptive data mean, sd etc
print("Columns:\n",df.columns) #column names
print("Shape:\n",df.shape)

# missing values

print("MISSING VALUES")
print("Total missing values per column:",df.isnull().sum())#total missing values per column
print("Rows with missing values:",df[df.isnull().any(axis=1)]) #rows with missing values

# BASIC STATISTICS

print("Mean of salary column:",df['Salary'].mean()) #mean of salary
print("Mean of performance rating:",df['PerformanceRating'].mean()) #mean of performance rating
print("Frequency count of IDs:",df['ID'].value_counts()) #frequency

# FILTERING/ SELECTING DATA

print("FILTERING/ SELECTING DATA")
print("Employees with salary greater than 50000:\n",df[df['Salary']>750000]) #employees with salary greater than 50000
print("Employees with performance rating greater than 3:\n",df[df['PerformanceRating']>3]) #employees with performance rating greater than 3
print("Employees with salary greater than 50000 and performance rating greater than 3:\n",df[(df['Salary']>50000) & (df['PerformanceRating']>3)]) #employees with salary greater than 50000 and performance rating greater than 3
print("Employees with salary greater than 50000 or performance rating greater than 3:\n",df[(df['Salary']>50000) | (df['PerformanceRating']>3)]) #employees with salary greater than 50000 or performance rating greater than 3


# GROUP BY AND AGGREGATION

print("GROUP BY AND AGGREGATION")
print("Average salary by department:\n",df.groupby('Department')['Salary'].mean()) #average salary by department
print("sum of salary by department",df.groupby('Department')['Salary'].sum()) #sum of salary by department

# SORTING DATA
print("SORTING DATA")
print("Sorting by salary:\n",df.sort_values(by='Salary',ascending=False)) #sorting by salary
print("Sorting by performance rating:\n",df.sort_values(by='PerformanceRating',ascending=False)) #sorting by performance rating