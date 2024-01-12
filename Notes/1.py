import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('worldometer_data.csv')
type(df)
df1 = df['Population']


