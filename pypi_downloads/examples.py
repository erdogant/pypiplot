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

# import seaborn as sns
# idx= ['aaa','bbb','ccc','ddd','eee']
# cols = list('ABCD')
# df = pd.DataFrame(abs(np.random.randn(5,4)), index=idx, columns=cols)

# # _r reverses the normal order of the color map 'RdYlGn'
# sns.heatmap(dfnew, cmap='RdYlGn_r', linewidths=0.5, annot=False)
