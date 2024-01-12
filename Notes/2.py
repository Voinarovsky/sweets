import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

def background_gradient(s, m, M, cmap='PuBu', low=0, high=0):
    rng = M - m
    norm = colors.Normalize(m - (rng * low),
                            M + (rng * high))
    normed = norm(s.values)
    c = [colors.rgb2hex(x) for x in plt.cm.get_cmap(cmap)(normed)]
    return ['background-color: %s' % color for color in c]

df = pd.DataFrame([[3,2,10,4],[20,1,3,2],[5,4,6,1]])
df.style.apply(background_gradient,
               cmap='PuBu',
               m=df.min().min(),
               M=df.max().max(),
               low=0,
               high=0.2)
