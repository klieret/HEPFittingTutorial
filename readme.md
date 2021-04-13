# HEP Fitting Tutorial

Originally by [Kilian Lieret](https://github.com/klieret)

Jupyter notebooks preview is available [here](https://nbviewer.jupyter.org/github/nikoladze/HEPFittingTutorial/tree/master/examples/jupyter_notebooks/).

To run the tutorial, just click on:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nikoladze/HEPFittingTutorial/master?filepath=examples%2Fjupyter_notebooks)



## Contents

* Fitting basics: Minmize a cost function using ``scipy.optimize.minimize``
* Fitting polynomials to points using ``np.polyfit``
* Fitting arbitrary functions to points using ``scipy.optimize.curve_fit``
* Template fits using ``pyroofit``
* Histogram template fits using ``pyhf``
* Hypothesis tests with ``pyhf``


## Setup instructions

If you want to use what you learned in the tutorial on your projects later, here are some examples how you can setup the nescessary software:

### Generic

If you don't have anything setup and need both ROOT and the python packages, the easiest way is through [Anaconda](https://www.anaconda.com/products/individual#Downloads) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). After installing, create your environment using

```
conda env create -f environment.yml
```

and activate it via

```
conda activate HEPFittingTutorial
```

### LMU Bachelor projects

#### On kuhrios (for Belle II projects)

Most tutorials should run on top of the latest Belle II release which you can set up with

```
source ~/setup_belle2.sh
```

You can then install the additional packages used in this tutorial on top with

```
pip3 install --user pyroofit pyhf iminuit mplhep
```

You should then be able to run the examples in a jupyter notebook or in jupyter hub (on Jupyter hub, make sure you use the Belle II Kernel with the latest version).

Note: Some of the packages have stopped supporting `python3.6`, so if you need the latest versions, maybe go for the [Generic installation with conda](#generic), e.g install Miniconda into your home directory.

#### On gar-ws-etp* (for ATLAS projects)

You can install the packages on top of the ROOT + python3.7 setup:

```
module load root/6.20.04_py3.7
```

To give newer versions of python packages you install as a user priority over the system environment, reset the `PYTHONPATH` to just contain ROOT

```
export PYTHONPATH=/software/opt/bionic/x86_64/root/6.20.04_py3.7/lib
```

Then you can install what is used in the tutorial with

```
pip install --user --upgrade pyroofit pyhf iminuit mplhep
```

Then you should be able to run the examples in a jupyter notebook.
