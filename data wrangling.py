# Data-Science-preparing the data for analysis
For the data science/data analysis
# Missing data or problematic/incorrect values in a dataset;
# Data are formatted incorrectly, preventing the analyst from working with the data in the right way;
# Data are spread across multiple files or data tables;
# Data are in the wrong "shape" for analysis and visualization
# Import generally needed library:
# In order to know about the data set properties, we can use some visualization like histogram, scatter plot between two features. 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import 


FILTERING
### WRANGLING STEP-BY-STEP
"""1. READING FILES, SELECTING COLUMNS, AND SUMMARIZING
   2. FILTERING AND SORTING
   3. RENAMING, ADDING, AND REMOVING COLUMNS
   4. SPLIT, APPLY, AND COMBINE
   5. SELECTION MULTIPLE COLUMNS AND FILTERING ROWS
   6. JOINING AND MERGING DATAFRAMES
   7. OTHER COMMONLY USED FEATURES
   8. OTHER LESS USED FEATURES"""
# reading the data:
data=pd.read_table('filename')
data=pd.read_csv('filename',sep=',',header=0,names=colume_name_list,index_col='user_id',
                     dtype={'zip_code':str}) #sep='+/s' space, sep='+/t' tab
# Detail description of the data set:
data.head()
data.dtypes #column name with type
data.shape  #numbers of observations and variables
data.index
data.columns #list of column name
data.values  #list of data
data.info()
# select a column:
data['column_name']
data.column_name
# summarize the data:
#general: describe numeric column
data.describe()
#describe top[first] freq
