#One-Hot Encoding

import pandas as pd # type: ignore
#Creating a dataframe of Phones (without names) , ID - SIZE - COLOUR
df = pd.DataFrame({'ID':[1,2,3,4,5,6,7,8,9,10] , 'Diagonal_screen_size':[6.55,6.7,6.6,6,6.2,6.6,6.55,6.7,6.55,6.6] , 'Colour':['Green','Blue','Red','Blue','Yellow','Black','Green','Yellow','Red','Grey']})

#Makes a list of object type columns (which are to be encoded)
object_cols = [col for col in df.columns if df[col].dtype=='object']
    
#One-Hot Encoding
for object_col in object_cols:
    #Makes a list of all possible value of a categorical variable (object_col)
    items = list(set(df[object_col]))
    cols = {}
    for item in items:
        bool_ls = []
        for i in df[object_col]:
            if i == item:
                bool_ls.append(1)
            else:
                bool_ls.append(0)
        cols[item] = bool_ls
    df=df.drop(object_col,axis=1)
    index = len(df.columns)
    for col in cols:
        df.insert(index,col,cols[col],True)
print(df)
        
