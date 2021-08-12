# HEP Fitting Tutorial
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/klieret/HEPFittingTutorial/master?filepath=examples%2Fjupyter_notebooks)
[![License](https://img.shields.io/github/license/klieret/HEPFittingTutorial.svg)](https://github.com/klieret/HEPFittingTutorial/blob/master/LICENSE.txt)
[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

## The material

Jupyter notebooks preview is available [here](https://nbviewer.jupyter.org/github/klieret/HEPFittingTutorial/tree/master/examples/jupyter_notebooks/).

To run the tutorial, just click on:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/klieret/HEPFittingTutorial/master?filepath=examples%2Fjupyter_notebooks)

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://gitlab.com/nikoladze"><img src="https://avatars.githubusercontent.com/u/3707225?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nikolai Hartmann</b></sub></a><br /><a href="https://github.com/klieret/HEPFittingTutorial/commits?author=nikoladze" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ThomasLueck"><img src="https://avatars.githubusercontent.com/u/49987770?v=4?s=100" width="100px;" alt=""/><br /><sub><b>ThomasLueck</b></sub></a><br /><a href="https://github.com/klieret/HEPFittingTutorial/commits?author=ThomasLueck" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
