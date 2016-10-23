import pandas as pd
import numpy as np

df = pd.read_csv('tableAfromStage1.csv')
dataFrame = df.replace('None', np.nan)

dataFrame.to_csv('tableA.csv', index=False)