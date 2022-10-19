import pandas as pd

try:
    df = pd.read_csv('test.cs')
    print(df.info)
except IOError as e:
    print("In here")
    print(e)
