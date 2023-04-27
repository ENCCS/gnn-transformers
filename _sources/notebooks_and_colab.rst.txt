Notebooks and Colab
===================

This workshop is structured in a number of Jupyter Notebooks developed for Google Colaboratory.

Before you start working on each notebook, make sure to make a copy of it to your own drive, otherwise any changes to do will not be saved.

The notebooks make use of `condacolab <https://github.com/conda-incubator/condacolab>`_,
a python packages which automates installed Anaconda distributions on a colab instance. 
This makes dealing with complex depencies a lot easier, since we can use Anaconda for 
package management instead of `pip`.

Most notebooks will contain a _preamble_, a section which deals with installing conda 
colab and the python dependencies for that notebook. The first cell in these will typically 
install condacolab and restart the python kernel. The following cells should be executed once 
the kernel has restarted and will install the dependencies which takes between 5 and 10 minutes.