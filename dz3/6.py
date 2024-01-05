import pandas as pd
import matplotlib
df = pd.read_csv('https://raw.githubusercontent.com/Voinarovsky/sweets/master/dz3/yandex_tracks_top100.csv')
# df['track_len'].plot(kind='kde')
print(df)