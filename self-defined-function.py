import pandas as pd
data=pd.read_csv()
data1=data.dropna()
data1.head()
data1['length']=data1.choice_description.apply(len)
topping=list(data1[data1.length==201].choice_description)
topping
dd={'choice':topping}
ddd=pd.DataFrame(dd)
ddd
x=ddd.choice.str.split(pat=',',expand=True) #split the choice description into different columns
columns=['Fresh Tomato Salsa (Mild)','Tomatillo-Green Chili Salsa (Medium)', 'Roasted Chili Corn Salsa (Medium)', 'Tomatillo-Red Chili Salsa (Hot)', 'Pinto Beans', 'Rice', 'Fajita Veggies', 'Cheese', 'Sour Cream', 'Lettuce']
x.columns=columns
#to count some topping per order/whole topping menu needed
def count(y):
  top1=0
  for i in range(len(list(data1.choice_description))):
    if y in list(data1.choice_description)[i]:
      top1+=1
  x.loc[0,y]=top1
for n in columns:  #applied with the whole topping menu
  count(n)
