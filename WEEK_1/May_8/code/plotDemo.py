import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [4, 5, 6], width=0.2) #sample bar plot
plt.title("Sample Bar Plot") #title of the plot
plt.xlabel("X-axis") #x-axis label
plt.ylabel("Y-axis") #y-axis label
plt.show() #show the plot
plt.savefig("sample_plot.png") #save the plot as png file
plt.close() #close the plot
