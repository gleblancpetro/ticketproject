from google.colab import files
import pandas as pd
import io
from datetime import date

your_file = files.upload()
filename = next(iter(your_file))

df = pd.read_csv(io.BytesIO(your_file[filename]))

d1 = date.today().strftime("%m-%d-%Y")

nec_columns = ['CUSTOMER', 'CUSTOMER NAME', 'CUSTOMER REFERENCE NO', 'ORDER DATE',
                'ORDER NO', 'CYCLE','ORDER AMOUNT','IN', 'OUT']

df1 = df[nec_columns]

types = df1['IN'].unique()

for i in types:
  
    df2 = df1.loc[df1['IN'] == i]
    df2['ORDER DATE'] = pd.to_datetime(df2['ORDER DATE'])
    df2 = df2.sort_values(by='ORDER DATE')
    df2 = df2.to_csv(f'{i}_OPEN_TICKET_{d1}.csv')
    files.download(f'{i}_OPEN_TICKET_{d1}.csv')
