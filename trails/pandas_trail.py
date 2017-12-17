import pandas as pd

#extracting the csv file as data frame
df = pd.read_csv('diamonds.csv', delimiter=',')

'''diamonds.csv is a data frame and we are trying to extract the data of all the diamonds having 'Ideal' cut'''


Ideal_cut = df.where(df['cut']=='Ideal').dropna(thresh=2)
#dropna is used to delete all the data which has Nan as its parameter values

print(Ideal_cut)
