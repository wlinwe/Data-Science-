##**Some tips for data analysis(common use syntax):**
###1. create dictionary:
#list can be a array or simple value
d={'key':list}
d['key']=value
#use two matched array create dictionary:
def dictionary:
  d={}
  for p in range(len(order_sum)):
    d[order_sum.index[p]]=order_sum[p]
d
###counting 
burrito=0
topping=0
for i in range(data.shape[0]):
  if 'Burrito' in data.iloc[i,2]:
    burrito+=1
    topping+=data.iloc[i,3].count(',')+1

quantities=topping/burrito
quantities  
#except counting what actual topping is, count the delimiter will be easier.
