# PivotTable: The hot new ML method of 2020

## Overview

* Pivot tables are linear models and we should evaluate/appreciate them
  as such. I want to convince you to take pivot tables seriously as a
  model and also show how we can expand on pivot tables as a serious
  part of the modeling process.
* Benefit: pivot tables can have surprisingly good performance
  * Link that paper about classification
  * DAG fixed effect logic
* Benefit: pivot tables are super fast to "train" even in Excel and
  super interpretable
  * If we think of them as a super basic fixed effects model there are
    even super fast gpu accelerated ways to train gigantic pivot tables
  * So interpretable people don't think about them as models
* A lot of the downsides of pivot tables can be formalized
  * Have you ever made both a count and a mean column in your pivot
    table? Then you've discovered the need for regularization and the
    James-Stein paradox. We could imagine a hierarchical Bayes pivot.
  * Dealing with continuous categories:
  * Looking at a pivot table and not believing the results because of
    confouding -- if you think this is just a linear model then add more
    controls (when available)
  * I have two pivot tables and I don't know how to "combine" them --
    the Frisch-Waugh-Lovell theorem will do this for you
  * Are these two groups "really" different -- we have statistical tests
  * Changing interpretation by changing linear form -- adding
    intercept/main effects


## Running the project

This is your new Kedro project, which was generated using `Kedro 0.15.4` by running:

```
kedro new
```

Take a look at the [documentation](https://kedro.readthedocs.io) to get started.

### Rules and guidelines

In order to get the best out of the template:
 * Please don't remove any lines from the `.gitignore` file provided
 * Make sure your results can be reproduced by adding necessary data to `data/01_raw` only
 * Don't commit any data to your repository
 * Don't commit any credentials or local configuration to your repository
 * Keep all credentials or local configuration in `conf/local/`

### Installing dependencies

Dependencies should be declared in `src/requirements.txt`.

To install them, run:

```
kedro install
```

### Running Kedro

You can run your Kedro project with:

```
kedro run
```

### Testing Kedro

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests with the following command:

```
kedro test
```

To configure the coverage threshold, please have a look at the file `.coveragerc`.


#### Working with Kedro from notebooks

In order to use notebooks in your Kedro project, you need to install Jupyter:

```
   pip install jupyter
```

For using Jupyter Lab, you need to install it:

```
pip install jupyterlab
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

You can also start Jupyter Lab:

```
kedro jupyter lab
```

And if you want to run an IPython session:

```
kedro ipython
```

Running Jupyter or IPython this way provides the following variables in
scope: `proj_dir`, `proj_name`, `conf`, `io`, `parameters` and `startup_error`.

##### Ignoring notebook output cells in `git`

In order to automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be left intact locally.

### Package the project

In order to package the project's Python code in `.egg` and / or a `.wheel` file, you can run:

```
kedro package
```

After running that, you can find the two packages in `src/dist/`.

### Building API documentation

To build API docs for your code using Sphinx, run:

```
kedro build-docs
```

See your documentation by opening `docs/build/html/index.html`.
