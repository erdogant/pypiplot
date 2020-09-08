# %%
# import pypi_downloads
# print(pypi_downloads.__version__)

from pypi_downloads import pypi_downloads
print(dir(pypi_downloads))

# %%
pp = pypi_downloads(username='erdogant')
pp.update()

# %%
pp = pypi_downloads(username='erdogant')

pp.stats(repo='bnlearn')
pp.stats(repo='distfit')
pp.stats(repo='worldmap')
pp.stats(repo='hnet')
pp.stats(repo='ismember')
pp.stats(repo='flameplot')
pp.stats(repo='pca')
pp.stats(repo=['df2onehot','pca','bnlearn','ismember','thompson'])
pp.stats()

# %%
from datetime import datetime, timedelta
from ismember import ismember
import pandas as pd
import numpy as np

df = pp.results.copy()
df = df.sum(axis=1)
nr_days = 7 # This is the number of rows in the plot
duration = 364 # This is the number of columns in the plot
firstday = 'Sunday'

# Set firstday as starting day
idx_start = np.where(df.index.day_name()[0:nr_days]==firstday)[0][0]
df = df.iloc[idx_start:]

# Make sure dataset an be devided by nr_days
extend_days = nr_days - np.mod(df.shape[0], nr_days)
end_date = datetime.now() + timedelta(float(extend_days-1))
extend_dates = pd.date_range(start=df.index[-1] + timedelta(1), end=end_date)
extend_dates = pd.DataFrame(index=extend_dates, data=np.zeros(len(extend_dates)))
dfnew = pd.concat([df, extend_dates])


# Get date until last year
dt = datetime.now()-timedelta(duration)
date_cols = pd.date_range(start=dt, end=datetime.now())
date_cols_str = date_cols.strftime('%Y-%m-%d').values

uimonths = np.unique(date_cols.month_name().values, return_index=True)
monthname = list(map(lambda x: x[0:3], uimonths[0]))
dfnew = pd.DataFrame(np.zeros((nr_days, len(date_cols)), dtype=int), columns=date_cols_str)
dfnew.columns = np.repeat('', dfnew.shape[1])
# Set date to short date annotation
dfnew.columns.values[uimonths[1]] = monthname 

# Find overlap
IA, idx = ismember(df.index.strftime('%Y-%m-%d').values, dfnew.columns.values)
row_idx = np.mod(np.arange(0, df.shape[0]), nr_days)
dfnew.iloc[row_idx, idx] = df.values

Iloc = row_idx==0
dfnew.iloc[0, idx[Iloc]] = df.loc[Iloc].values

dfnew.iloc[[0,1,2,3,4,5], [0,1,2,3,4,5]] = [1,1,1,1,1]


datelist = pd.date_range(datetime.datetime.today(), periods=100).tolist()

import seaborn as sns
idx= ['aaa','bbb','ccc','ddd','eee']
cols = list('ABCD')
df = pd.DataFrame(abs(np.random.randn(5,4)), index=idx, columns=cols)

# _r reverses the normal order of the color map 'RdYlGn'
sns.heatmap(dfnew, cmap='RdYlGn_r', linewidths=0.5, annot=False)
