# pypi_downloads

[![Python](https://img.shields.io/pypi/pyversions/pypi_downloads)](https://img.shields.io/pypi/pyversions/pypi_downloads)
[![PyPI Version](https://img.shields.io/pypi/v/pypi_downloads)](https://pypi.org/project/pypi_downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/pypi_downloads/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/pypi_downloads/month)](https://pepy.tech/project/pypi_downloads/month)
[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)
[![Sphinx](https://img.shields.io/badge/Sphinx-Docs-blue)](https://erdogant.github.io/pypi_downloads/)


* pypi_downloads is Python package

### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install pypi_downloads from PyPI (recommended). pypi_downloads is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_pypi_downloads python=3.7
conda activate env_pypi_downloads
```

```bash
pip install pypi_downloads            # normal install
pip install --upgrade pypi_downloads # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/erdogant/pypi_downloads.git@0.1.0#egg=master
pip install git+https://github.com/erdogant/pypi_downloads#egg=master
pip install git+https://github.com/erdogant/pypi_downloads

# By cloning
git clone https://github.com/erdogant/pypi_downloads.git
cd pypi_downloads
pip install -U .
```  

#### Import pypi_downloads package
```python
import pypi_downloads as pypi_downloads
```

#### Example:
```python
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/pypi_downloads/data/example_data.csv')
model = pypi_downloads.fit(df)
G = pypi_downloads.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/pypi_downloads/blob/master/docs/figs/fig1.png" width="600" />
  
</p>


#### Citation
Please cite pypi_downloads in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2020pypi_downloads,
  title={pypi_downloads},
  author={Erdogan Taskesen},
  year={2020},
  howpublished={\url{https://github.com/erdogant/pypi_downloads}},
}
```

#### References
* https://github.com/erdogant/pypi_downloads

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated :)
	Star it if you like it!
