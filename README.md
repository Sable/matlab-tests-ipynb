DEPRECATED: *We now favor a definition of tests in pure MATLAB that does not depend in IPython Notebook because our static compilers do not play well with it. See https://github.com/Sable/matlab-tests for the most recent suite.*

# matlab-tests-ipynb

Collection of unit tests and expected results to check compliance with the MATLAB semantics.

The tests are specified using the [Jupyter Notebook format](http://nbformat.readthedocs.org/en/latest/format_description.html#notebook-file-format), a JSON format that stores the result of an interactive session in a [Jupyter Notebook](http://jupyter-notebook.readthedocs.org/en/latest/notebook.html) with a [Jupyter Kernel](http://jupyter-client.readthedocs.org/en/latest/kernels.html), in this case a MATLAB-compatible one.

The tests are grouped according to features of the language that are related from a compiler/virtual-machine implementer perspective. The end goal is to be able to concisely define the scope of support for implementations by the names of the suite of tests (Notebooks) they run correctly (ex: scalar-arithmetic, 1d-array). An implementation should include a runner script that automatically runs the specified suites to ease verification of correctness by a third-party. That should make the job of us poor grad students easier, both for (1) taking ownership of previous projects once the original developer left for greener pastures and for (2) reviewing artifacts/papers for conferences ;-).


# Contributing

The quickest way to contribute new tests is to:

1. Install the Jupyter Notebook through an existing Python distribution, such as [Canopy Python](https://www.enthought.com/products/canopy/)
2. Install 'pip' from that distribution
3. Install MATLAB
4. Install the [MATLAB kernel](https://pypi.python.org/pypi/matlab_kernel) for IPython with 'pip install matlab_kernel'
5. Start the IPython Notebook within the 'matlab-tests' directory with 'ipython notebook'
6. Add tests within a single suite (Notebook) or add a new suite (Notebook)
7. Do a pull request

# Citation

At the moment, no formal publication has been made about this suite. Please simply refer to the repository on Github as https://github.com/Sable/matlab-tests-ipynb.

