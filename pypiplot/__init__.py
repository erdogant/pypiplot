from pypiplot.pypiplot import Pypiplot

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '2.0.0'

# module level doc-string
__doc__ = """
pypiplot
=====================================================================

Description
-----------
Python package to count and plot the number of downloads from Pypi.

Example
-------
>>> from pypiplot import Pypiplot
>>> pp = Pypiplot(username='erdogant')
>>> pp.update()
>>> pp.stats()
>>> pp.plot_cal()
>>> pp.plot_year()
>>> pp.plot()
>>>
>>> # Selected repos
>>> pp.update(repo=['df2onehot','pca','bnlearn','ismember','thompson'])
>>> # Compute download statistics
>>> pp.stats(repo=['df2onehot','pca','bnlearn','ismember','thompson'])
>>> # Make plot
>>> pp.plot_year()
>>> pp.plot()

References
----------
* https://github.com/erdogant/pypiplot

"""
