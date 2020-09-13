# pypiplot

[![Python](https://img.shields.io/pypi/pyversions/pypiplot)](https://img.shields.io/pypi/pyversions/pypiplot)
[![PyPI Version](https://img.shields.io/pypi/v/pypiplot)](https://pypi.org/project/pypiplot/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/pypiplot/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/pypiplot/month)](https://pepy.tech/project/pypiplot/month)
[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)
[![Sphinx](https://img.shields.io/badge/Sphinx-Docs-blue)](https://erdogant.github.io/pypiplot/)


* pypiplot is Python package

### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install pypiplot from PyPI (recommended). pypiplot is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_pypiplot python=3.7
conda activate env_pypiplot
```

```bash
pip install pypiplot            # normal install
pip install --upgrade pypiplot # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/erdogant/pypiplot.git@0.1.0#egg=master
pip install git+https://github.com/erdogant/pypiplot#egg=master
pip install git+https://github.com/erdogant/pypiplot

# By cloning
git clone https://github.com/erdogant/pypiplot.git
cd pypiplot
pip install -U .
```  

#### Import pypiplot package
```python
import pypiplot as pypiplot
```

#### Example:
```python
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/pypiplot/data/example_data.csv')
model = pypiplot.fit(df)
G = pypiplot.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/pypiplot/blob/master/docs/figs/fig1.png" width="600" />
</p>


#### Citation
Please cite pypiplot in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2020pypiplot,
  title={pypiplot},
  author={Erdogan Taskesen},
  year={2020},
  howpublished={\url{https://github.com/erdogant/pypiplot}},
}
```

#### References
* https://github.com/erdogant/pypiplot

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated :)
	Star it if you like it!
