import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#boxplot 
#defecting groups of numericals data through their quartiles
# determining outliers in datasets
df = sns.load_dataset("tips")
dd = df.boxplot(by = "day",column = ["total_bill"],grid = True)
plt.show()

#displot 
#gives histogram
#distribution of peoples based on age / density of data
titanic = sns.load_dataset("titanic")
titanic.head()
age1 = titanic["age"].dropna() #dropna remove all null value
age1.head()

sns.distplot(age1,bins=30,kde = False)

#regplot
# when using linear regression model
#re 
data = sns.load_dataset("mpg")
data.head()
sns.regplot(x="mpg",y="acceleration",data= data)
plt.show()
