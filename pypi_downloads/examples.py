# %%
# import pypi_downloads
# print(pypi_downloads.__version__)

from pypi_downloads import pypi_downloads
print(dir(pypi_downloads))

# %%
pp = pypi_downloads(username='erdogant')

# %% Update all
pp.update()

# %% Update single repo
pp.update(repo='bnlearn')
pp.stats(repo=['df2onehot','pca','bnlearn','ismember','thompson'])

# %%
pp = pypi_downloads(username='erdogant')

pp.stats(repo='distfit')
pp.stats(repo='worldmap')
pp.stats(repo='hnet')
pp.stats(repo='ismember')
pp.stats(repo='flameplot')
pp.stats(repo='pca')
pp.stats(repo=['df2onehot','pca','bnlearn','ismember','thompson'])

# %% Plot bnlearn
pp.stats(repo='benfordslaw')
pp.plot(vmin=1)

# %% Plot
path = 'D://PY/REPOSITORIES/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html'
pp.stats()
pp.plot(path=path, vmin=700)

# %%
from datetime import datetime, timedelta
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
df_end = pd.DataFrame(index=extend_dates, data=np.zeros(len(extend_dates)))


# getdates = df_ext.index.strftime('%Y-%m-%d')
date_start = df.index[0]
# colnames = df_ext.index.month_name().values.reshape((-1, nr_days))[:,-1]
# df_ext = pd.DataFrame(df_ext.values.reshape((-1, nr_days)), index=colnames).T


# Now we need to make a table that has 365 columns and 7 rows.
missing_days = duration-df_ext.shape[0]
dt = date_start-timedelta(missing_days)
date_cols = pd.date_range(start=dt, end=date_start)[:-1]
df_start = pd.DataFrame(np.zeros((len(date_cols), 1)), dtype=int, index=date_cols)

# Final matrix
df_fin = pd.concat([df_start, df, df_end], axis=0)

df_heatmap = df_fin.values.reshape((-1, nr_days))
df_heatmap = pd.DataFrame(data=df_heatmap.T, columns=)




# %%
from datetime import datetime, timedelta
from ismember import ismember
import pandas as pd
import numpy as np
import seaborn as sns

df = pp.results.copy()
df = df.sum(axis=1)
nr_days = 7 # This is the number of rows in the plot
duration = 365 # This is the number of columns in the plot
firstday = 'Sunday'

# Set firstday as starting day
idx_start = np.where(df.index.day_name()[0:nr_days]==firstday)[0][0]
df = df.iloc[idx_start:]

# Make sure dataset an be devided by nr_days
extend_days = nr_days - np.mod(df.shape[0], nr_days)
end_date = datetime.now() + timedelta(float(extend_days-1))
extend_dates = pd.date_range(start=df.index[-1] + timedelta(1), end=end_date)
extend_dates = pd.DataFrame(index=extend_dates, data=np.zeros(len(extend_dates)))
df_ext = pd.concat([df, extend_dates])

# getdates = df_ext.index.strftime('%Y-%m-%d')
date_start = df_ext.index[0]
colnames = df_ext.index.month_name().values.reshape((-1, nr_days))[:,-1]
df_ext = pd.DataFrame(df_ext.values.reshape((-1, nr_days)), index=colnames).T

# df_ext.columns.values = getdates.values


# Now we need to make a table that has 365 columns and 7 rows.
missing_days = duration-df_ext.shape[0]*df_ext.shape[1]
makecols = np.int(np.floor((missing_days)/nr_days))
df_final = pd.DataFrame(np.zeros((nr_days, makecols), dtype=int))

dt = date_start-timedelta(missing_days)
date_cols = pd.date_range(start=dt, end=date_start)[:-1]
colnames = date_cols.month_name()

idx=np.arange(0, len(colnames), np.int(np.floor(len(colnames)/df_final.shape[1])))
idx = idx[-df_final.shape[1]:]
# idx = idx[0:df_final.shape[1]]
df_final.columns = colnames[idx]

# Make final dataframe
df_final = pd.concat([df_final, df_ext], axis=1)

# Set month
uimonths = np.unique(df_final.columns.values, return_index=True)
monthname = list(map(lambda x: x[0:3], uimonths[0]))

df_final.columns = np.repeat('', df_final.shape[1])
# Set date to short date annotation
df_final.columns.values[uimonths[1]] = monthname 

# %%
import imagesc
imagesc.plot(df_final.values)
A = imagesc.seaborn(df_final.values, df_final.index.values, df_final.columns.values)
D = imagesc.seaborn(df_final.values, df_final.index.values, df_final.columns.values, annot=False, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,4))
sns.heatmap(df_final, cmap='RdYlGn_r', linewidths=0.5, annot=False, linecolor='#ffffff')


# %%
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
