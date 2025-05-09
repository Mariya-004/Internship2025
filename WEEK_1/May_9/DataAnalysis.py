import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:

    def __init__(self, fileName): #constructor to take the file name and read it
        self.fileName = fileName
        self.data = pd.read_csv(fileName)
        print("Data read successfully")
    
    def getData(self): #to get the data
        return self.data
    
    def getSummary(self): #to get the summary of the data
        return self.data.describe()
    
    def initialInspection(self):
        print("Initial Inspection of the data")
        print("Shape of the data:", self.data.shape)
        print("Columns in the data:", self.data.columns)
        print("Data types of the columns:", self.data.dtypes)
        print("Missing values in the data:", self.data.isnull().sum())
        print("First 5 rows of the data:")
        print(self.data.head())

    def groupBy(self, column1,column2):
        print("Grouping the data by", column1+" and calculating the mean of"+ column2)
        groupedData = self.data.groupby(column1)[column2].mean()
        print(groupedData)
        return groupedData
    
    def plotData(self, x, y):
        print("Plotting the data")
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title("Plot of " + y + " vs " + x)
        plt.show()
#main function
fileName=input("Enter the filename:")
dataAnalysis = DataAnalysis(fileName)
print("DATA")
data = dataAnalysis.getData()
print("Summary of data")
summary=dataAnalysis.getSummary()
print("Initial inspection")
initInspec=dataAnalysis.initialInspection()
col1=input("Enter the column name to group by:")
col2=input("Enter the column name to group by:")
groupedData=dataAnalysis.groupBy(col1,col2)
x=input("Enter the x-axis column name:")
y=input("Enter the y-axis column name:")
dataAnalysis.plotData(x, y)