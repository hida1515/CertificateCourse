# import pandas as pd
# s = pd.Series([10,20,30,40])
# data = {'Name':['Tony Stark','Steve Rogers','Bruce Banner','Clint Barton','Natasha Romanoff','Thor Odinson'],'Age':[42,105,44,42,42,None]}
#df = pd.DataFrame(data)
#print(f"\n{df.head()}")
#print(f"\n{df.head(3)}")
#print(df.tail())
#print(f"\n{df.tail(2)}")
#print(df.info())
#print(df.describe())
#print(df.columns)
#print(df.shape)

# df = pd.DataFrame(data,index=['a','b','c','d','e','f'])
#print(df.loc['a':'c'])
#print(df.loc['a','Name'])

#print(df.iloc[0])
#print(df.iloc[1,0])
#print(df.iloc[:,0:2])
#print(df.isnull())
#print(df.dropna())  #drops the null row
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# print(df)



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# x = np.linspace(0,20,100)
# y = np.sin(x)
# plt.plot(x,y,color='pink',linestyle='--',marker='o')
# plt.title("line-plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x,y,color="red",marker='x')
# plt.title("scatter plot")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# cartegories = ['a','b','c']
# values = [4,7,9]
# plt.bar(cartegories,values,color = ['red','green','orange'])
# plt.title("bar plot")
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# cartegories = ['nit','iim','devagiri']
# values = [4,7,9]
# plt.barh(cartegories,values,color = ['red','blue','black'])
# plt.title(" horizontal bar plot")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# data = np.random.randn(1000)
# plt.hist(data,bins=30,color='yellow',edgecolor='black')
# plt.title("histogram")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# sizes=[20,30,50,60,70]
# color=['black','green','red','yellow']
# plt.pie(sizes,colors=color,autopct ='%1.1f%%',startangle =90)
# plt.title("piechart")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# days = [1,2,3,4,5,6]
# eating = [2,3,4,6,8,9]
# working = [2,2,3,3,4,5]
# sleeping = [9,8,7,6,5,5]
# playing =[2,3,4]
# plt.stackplot(days,eating,working,sleeping,labels=['days','eating','work','sleep','play'])
# plt.legend(loc="upper left")
# plt.title("stacked area plot")
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# data = np.random.normal(100,30,200)
# plt.boxplot(data)
# plt.title("box plot")
# plt.show()


# import seaborn as sns
# df = sns.load_dataset("tips")



# import matplotlib.pyplot as plt

# import seaborn as sns
# df = sns.load_dataset("tips")
# sns.histplot(df["total_bill"],kde=True,bins=30,color="red")
# plt.title("histogram")
# plt.show()

# import seaborn as sns

# import matplotlib.pyplot as plt
# import pandas as pd
# data = pd.DataFrame({
# "cartegorie" : ['a','b','c'],
# "values" : [4,7,9]
# })

# sns.barplot(x="cartegorie",y="values",data=data)
# plt.title(" NORMAL bar plot")
# plt.show()




# import seaborn as sns
# df = sns.load_dataset("tips")

# import matplotlib.pyplot as plt
# sns.countplot(x="day",data=df,palette="Set2")
# plt.title("COUNT POLT")
# plt.show()


# import seaborn as sns
# df = sns.load_dataset("tips")
# import matplotlib.pyplot as plt
# sns.boxplot(x="day",y="total_bill",data=df,palette="pastel")
# plt.title("boxPloT")
# plt.show()


# import seaborn as sns
# df = sns.load_dataset("tips")
# import matplotlib.pyplot as plt
# sns.scatterplot(x="total_bill",y="tip",data=df,hue="sex",style="time")
# plt.title("scatter plot")
# plt.show()



