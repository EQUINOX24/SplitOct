# SplitOct

SplitOct is a Python library that provides an implementation of the algebra of split octonions. Split octonions are a variant of octonions, which are an eight-dimensional analog of complex numbers. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Split-octonions). This library allows you to perform various operations on split octonions, including addition, multiplication, inverse and conjugation for both numeric and symbolic expressions.

## Installation

To use SplitOct, you need to have SymPy installed as a dependency. SymPy is a Python library for symbolic mathematics. You can install SymPy using pip:

```
pip install sympy
```

After installing SymPy, you can clone the SplitOct repository or download the `SplitOct.py` file from the [GitHub repository](https://github.com/EQUINOX24/SplitOct/blob/master/src/SplitOct.py).

## Usage

It is highly recommended to use SplitOct with [JupyterLab](https://jupyterlab.readthedocs.io/) for an optimal user experience, particularly because JupyterLab can render TeX equations beautifully while displaying them. To use SplitOct in your Python code, you need to import the `SplitOct` class from the `SplitOct.py` module. Here's an example of how to import the class:

```python
from SplitOct import *
```

Once you have imported the class, you can create split octonion objects and perform various operations on them. Here are some examples:

```python
# Create split octonion objects
x = SplitOctonion( [1, 2, 3, 4, 5, 6, 7, 8] ) # one way to create a split octonionic number
y = 1 + 10*j1 - 4 *j3 - 5 * oI + J2 # another way

# Addition
w = x + y
print(w)  # Output: 2 + 12 j_{1} + 3 j_{2} + 6 J_{1} + 8 J_{2} + 8 J_{3}

# Division
z = x * y.inv()
print(z)  # Output: \frac{23}{91} + \frac{6 j_{1}}{13} - \frac{5 j_{2}}{91} + \frac{72 j_{3}}{91} - \frac{15 I}{91} + \frac{34 J_{1}}{91} + \frac{125 J_{2}}{91} - \frac{60 J_{3}}{91}
```

You can also perform arithmetic operations between split octonions and other numeric types.

```python
# Scaling
c = 2 * x 
print(c) # Output: 2 + 4 j_{1} + 6 j_{2} + 8 j_{3} + 10 I + 12 J_{1} + 14 J_{2} + 16 J_{3}
```

To view more examples see the jupyter notebook about split octonionic [identities](https://github.com/EQUINOX24/SplitOct/blob/master/src/nb0_splitoct_identities.ipynb).

## Contributing

If you want to contribute to SplitOct, you can fork the repository, make your changes, and submit a pull request. Contributions such as bug fixes, new features, or improvements are welcome.

## License

SplitOct is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPL-3.0). You are free to use, modify, and distribute this library in accordance with the terms and conditions of the GPL-3.0 license.
