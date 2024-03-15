# Environment setup for FOM

The following guide aim to help putting in place a Python environment able to run the downloadable FOM in addition to genrerate the data files required for their operation.

## Virtual environment setup

To create the environment in the directory "my-project-dir":
```shell
$ cd my-project-dir
$ python -m venv venv
```

To activate it:
```shell
$ source my-project-dir/venv/bin/activate
```
To check which Python installation will be used in the terminal:
```shell
(venv)$ which python
my-project-dir/venv/bin/python
```

%image ?

You can find more information about venv at <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>

## Dependencies installation

The required libraries are:
- Numpy
- Plotly
- 
The following command lines allow to install them: 

```shell 
$ pip install numpy
$ pip install plotly
```