Learn Python - The Hard Way
=========================
Set of simple programs written during learning **basics of Python** language 

based on *[Learn Python - The Hard Way](http://learnpythonthehardway.org/book/)* course.

:construction: Repository under construction. :construction:

### Requirements
* Windows, Linux or Mac OS X
* Python 2.7
* Pip (Python Package Manager)

### Installing Python
* on Linux: Most of the Linux distributions should have installed Python by default
* on Windows: Download Python at: https://www.python.org/downloads/windows/ and run installer
* on Mac OS X: Download Python at: https://www.python.org/downloads/mac-osx/

### Executing Python scripts from terminal
* on Linux: Most of the Linux distributions should have enabled Python by default, so simply open terminal and type *python* to see if everything works.
* on Windows: add */PythonXX* (e.g. *C:/Python27*) into *Path* environmental variable. Location of the Python directory depends on your configuration. Next, re-run terminal window and type `python`
* in order to check installed version of the Python, type: `python --version`
* in order to exit python console type `exit()`

### Installing Pip (Python Package Manager) on Windows
1. Download: https://raw.github.com/pypa/pip/master/contrib/get-pip.py script
2. Execute: `python get-pip.py`
3. *pip.exe* and *easy_install.exe* files now should be located at: */PythonXX/Scripts* (e.g. *C:/Python27/Scripts*)
4. Add */PythonXX/Scripts* (e.g. *C:/Python27/Scripts*) directory into *Path* environmental variable.
5. Re-run terminal window
6. Type `pip`, to check if package manager works
7. You can type `pip --version`, in order to check version of the pip

### Installing Pip on Linux (Ubuntu)
1. Open terminal
2. Type `sudo apt-get install python-pip`

#### Using Pip
* In order to install desired package just type `pip install desired_package` (e.g. `pip install Flask`)
* If you are working on Linux, type `sudo pip install desired_package` (e.g. `sudo pip install Flask`)
* Index of available packages can be found at: https://pypi.python.org/pypi/
* List of installed packages can be displayed with `pip freeze` command.

### Unit Testing
* UT in Python can be done with [nose](https://pypi.python.org/pypi/nose/). Install it via pip with the following command: `sudo pip install nose`
* UT can be also created with [unittest](https://docs.python.org/2/library/unittest.html) package provided with Python.

### Virtualenv

`virtualenv` is a tool to create isolated Python environments.

More information:
* [Overview on PyPi](https://pypi.python.org/pypi/virtualenv)
* [Virtualenv tutorial](http://simononsoftware.com/virtualenv-tutorial/)
* [A primer on virtualenv](http://iamzed.com/2009/05/07/a-primer-on-virtualenv/)

### Popular IDEs & editors
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Sublime Text](http://www.sublimetext.com/)
* [Atom](https://atom.io/)

### Popular Python web frameworks
* [Django](https://www.djangoproject.com/)
* [Flask](http://flask.pocoo.org/)
* [Bottle](http://bottlepy.org/)

### Resources
* https://www.python.org/
* http://learnpythonthehardway.org/book/
* http://www.codecademy.com/en/tracks/python
* http://www.diveintopython.net/

### License
MIT
