import pandas as pd
df = pd.read_csv("data/ambitionbox_all_cities.csv")
 # cleaned industry column
df["industry"] = df["industry"].str.split("|").str[0].str.strip()

 # save cleaned data 
df.to_csv("../data/ambitionbox_cleaned.csv",index = False)
print("Industry column data cleaned and saved successfully")