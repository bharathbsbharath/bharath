import pandas as pd

data = {
    'enames': ['roshan', 'amar', 'ashwin','nithin'],
    'types': ['regular', 'adhoc', 'regular','adhoc'],
    'department': ['cs', 'cs', 'ec','ec'],
    'experience': [10, 20, 5, 15],
    'salary': [50000, 15000, 30000,20000]
}

df = pd.DataFrame(data)

print(df)
