import pandas as pd 
from matplotlib import pyplot as plt
from pathlib import Path

n_wells = 2
data_types = ['raw', 'smooth']

# TODO glob all data, i.e. remove 1
data = Path('data').glob('*1.xlsx')
dataframes = []
for xlsx in data:
    df = pd.read_excel(xlsx, index_col = 0, engine = 'openpyxl')
    # renaming df index for clarity and brevity 
    index = []
    raw_smooth = 'smooth'
    for name in df.index.values.tolist():
        if 'raw' in name:
            raw_smooth = 'raw'
        # keep well.video.neuronID
        name = name[7:12]
        index.append('{}.{}'.format(name, raw_smooth))
    df.index = index
    dataframes.append(df)

for df in dataframes:
    pass
print(df)