# `Dendrogram`: N-Dimensional Dendrogram

[![version](https://img.shields.io/badge/version-v0.1.dev-brightgreen.svg?style=flat)](https://github.com/EnthalpyBill/Dentrogram)
[![license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

`Dendrogram` is a toolkit for creating N-dimensional (ND) dendrogram 

## Table of Contents

- [Intro](#intro)
- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
	- [Authors](#authors)
	- [Maintainers](#maintainers)
- [Cite](#cite)
- [License](#license)

## Intro

*Placeholder*

## Install

The prerequisites of `Dendrogram` are 

```
python >= 3.8
numpy >= 1.18
```

Lower versions may also work (and higher versions may not work). Please [raise an issue](https://github.com/EnthalpyBill/Dendrogram/issues/new) if it doesn't work for you. Next, you can `git clone` the source package from [GitHub](https://github.com/EnthalpyBill/Dendrogram):
```shell
$ git clone https://github.com/EnthalpyBill/Dendrogram.git
```
To build and install `Dendrogram`, `cd` the folder and `pip install` it:
```shell
$ cd Dendrogram/
$ pip install -e .
```
The `-e` command allows you to make changes to the code. Remove it if you don't want to do so. The package has not been published to `PyPI` yet. 

## Usage

To use the package, just import it as
```python
>>> import dendrogram as dg
```
The command below creates the clustering tree (a `structureTree.clusterTree` object) for the dendrogram:
```python
>>> tree = dg.makeTree(data, min_value, min_delta=0, min_npix=1, num_level=100)
```
`data` must be an ND histogram (i.e., a numpy ndarray). 

## Contribute

Feel free to dive in! [Raise an issue](https://github.com/EnthalpyBill/Dendrogram/issues/new) or submit pull requests.

### Authors

- [@mxmintaka (Xi Meng)](https://github.com/mxmintaka)
- [@EnthalpyBill (Bill Chen)](https://github.com/EnthalpyBill)

### Maintainers

- [@EnthalpyBill (Bill Chen)](https://github.com/EnthalpyBill)

## Cite

This README file is based on [Standard Readme](https://github.com/RichardLitt/standard-readme).

## License

`Dendrogram` is available at [GitHub](https://github.com/EnthalpyBill/Dendrogram) under the [MIT license](LICENSE).