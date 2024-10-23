#Ordinal Encoding

import pandas as pd # type: ignore
#Creating a dataframe of Phones (without names) , ID - SIZE - COLOUR
df = pd.DataFrame({'ID':[1,2,3,4,5,6,7,8,9,10] , 'Diagonal_screen_size':[6.55,6.7,6.6,6,6.2,6.6,6.55,6.7,6.55,6.6] , 'Colour':['Green','Blue','Red','Blue','Yellow','Black','Green','Yellow','Red','Grey']})

#Makes a list of object type columns (which are to be encoded)
object_cols = [col for col in df.columns if df[col].dtype=='object']
    
#Ordinal Encoding
for object_col in object_cols:
    #Makes a list of all possible value of a categorical variable and sorts them to assign a number
    items = list(set(df[object_col]))
    items.sort()
    #This is the index at which the variable column existed and now will be replaced by encoded one
    ind=len(df.columns)-1
    #Making a list
    new_ls = []
    for i in df[object_col]:
        new_ls.append(items.index(i)+1)
    df=df.drop(object_col,axis=1)
    df.insert(ind, object_col, new_ls, True)

    
    
   
