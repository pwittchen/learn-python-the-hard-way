Learn Python - The Hard Way
=========================

### Overview

Set of simple programs written during learning **basics of Python** language based on *[Learn Python - The Hard Way](http://learnpythonthehardway.org/book/)* course. All tasks can be found in *exercises* directory. In the same directory, we can found another `README.md` file including list of all tasks. Moreover, this `README.md` file includes **important and essential information concerning programming in Python**. You can also read [a short article about this project on my blog](http://wittchen.io/2015/09/01/learning-python/).

### Contents
* [Requirements](#requirements)
* [Installing Python](#installing-python)
* [Executing Python scripts from terminal](#executing-python-scripts-from-terminal)
* [Pip](#pip)
 * [Installing Pip on Windows](#installing-pip-on-windows)
 * [Installing Pip on Linux](#installing-pip-on-linux)
 * [Installing Pip on macOS](#installing-pip-on-macos)
 * [Using Pip](#using-pip)
* [Unit Testing](#unit-testing)
* [Virtualenv](#virtualenv)
* [Pipenv](#pipenv)
* [Pyenv](#pyenv)
* [Scripts on Linux](#scripts-on-linux)
* [Style Guide for Python Code](#style-guide-for-python-code)
* [Static code analysis](#static-code-analysis)
* [Development Environments](#development-environments)
* [Python web frameworks](#python-web-frameworks)
* [Useful Python libraries](#useful-python-libraries)
* [Tools written in Python](#tools-written-in-python)
* [Collections of tools written in Python](#collections-of-tools-written-in-python)
* [Resources](#resources)
* [Videos](#videos)
* [Books](#books)
* [License](#license)

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
* on Windows: add `/PythonXX` (e.g. `C:/Python27`) into `Path` environmental variable. Location of the Python directory depends on your configuration. Next, re-run terminal window and type `python`
* in order to check installed version of the Python, type: `python --version`
* in order to exit python console type `exit()`

### Pip
Pip is a Python Package Manager.

#### Installing Pip on Windows
1. Download: https://bootstrap.pypa.io/get-pip.py script
2. Execute: `python get-pip.py`
3. *pip.exe* and *easy_install.exe* files now should be located at: */PythonXX/Scripts* (e.g. *C:/Python27/Scripts*)
4. Add */PythonXX/Scripts* (e.g. *C:/Python27/Scripts*) directory into *Path* environmental variable.
5. Re-run terminal window
6. Type `pip`, to check if package manager works
7. You can type `pip --version`, in order to check version of the pip

#### Installing Pip on Linux
1. Open terminal
2. Type `sudo apt-get install python-pip`

#### Installing Pip on macOS
1. Open terminal
2. Type `brew install python3`

This command will install python and pip.

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
* [Virtual Environments on Python Guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### Pipenv

`pipenv` is Python Development Workflow for Humans.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages.

More information:
* https://github.com/pypa/pipenv

### Pyenv

[pyenv](https://github.com/pyenv/pyenv/) is a simple Python version management.

### Scripts on Linux

If we want to create a Python script for Linux, we should set the following header:

```python
#!/usr/bin/python -u

# your Python script code goes here...
```

After that when our script was saved in `script.py` file, we can execute our script as follows:

```
./script.py
```

### Style Guide for Python Code

**PEP 0008** is a current Style Guide for Python Code.

link: https://www.python.org/dev/peps/pep-0008/

code style: https://docs.python-guide.org/writing/style/

### Static Code Analysis

- [Pylint](https://www.pylint.org/)
- [Pytype (by Google)](https://github.com/google/pytype)
- [Review of Python static code analysis tools](https://blog.codacy.com/review-of-python-static-analysis-tools-ff8e7e27f972)
- [Awesome static analysis for Python](https://github.com/mre/awesome-static-analysis#python)

### Development Environments
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Sublime Text](http://www.sublimetext.com/)
* [Atom](https://atom.io/)

### Python web frameworks
* [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://github.com/tomchristie/django-rest-framework)
  * [Silk - smooth profiling for Django](https://github.com/mtford90/silk)
* [Flask](http://flask.pocoo.org/)
  * [Flask Restful](https://github.com/flask-restful/flask-restful)
  * [Flask Profiler](https://github.com/muatik/flask-profiler)
* [Bottle](http://bottlepy.org/)
* [Weppy](https://github.com/gi0baro/weppy)
* [Growler](https://github.com/pyGrowler/Growler)

### Web servers
* [Sanic - python 3.5+ web server that's written to go fast](https://github.com/channelcat/sanic)

### Useful Python libraries
* [Requests - HTTP requests for humans](https://github.com/kennethreitz/requests)
* [Httpie - CLI HTTP client](https://github.com/jkbrzt/httpie)
* [Python Rex - regular expressions for humans](https://github.com/cypreess/python-rex)
* [PythonVerbalExpressions - readable API for regular expressions](https://github.com/VerbalExpressions/PythonVerbalExpressions)
* [Envelopes - mailing for human beings](https://github.com/tomekwojcik/envelopes)
* [Tornado - web framework and asynchronous networking library](https://github.com/tornadoweb/tornado)
* [Schedule - Python job scheduling for humans](https://github.com/dbader/schedule)
* [Agate - data analysis for humans](https://github.com/onyxfish/agate)
* [Gspread - Google Spreadsheets Python API](https://github.com/burnash/gspread)
* [EFILTER (dotty) - a general-purpose destructuring and search language](https://github.com/google/dotty)
* [Scrapy - web crawling & scraping framework](https://github.com/scrapy/scrapy)
* [sh - Python process launching (allows you to call any program as if it were a function)](https://github.com/amoffat/sh)
* [furl - url parsing and manipulation](https://github.com/gruns/furl)

### Tools written in Python

* [Wifite - an automated wireless attack tool](https://github.com/derv82/wifite)
* [Glances - an Eye on your system](https://github.com/nicolargo/glances)
* [Pidcat - colored and improved logcat for Android apps](https://github.com/JakeWharton/pidcat)
* [Caffeine-plus - indicator preventing from turning screensaver/screenlock on](https://github.com/mildmojo/caffeine-plus)
* [Spaceship generator - a script for Blender](https://github.com/a1studmuffin/SpaceshipGenerator)
* [neighbourhood - Layer 2 network neighbourhood discovery tool that uses scapy](https://github.com/bwaldvogel/neighbourhood)
* [Routersploit - The Router Exploitation Framework](https://github.com/reverse-shell/routersploit)
* [scanless - port scanner](https://github.com/vesche/scanless)

### Collections of tools written in Python
* [Python Pentest Tools](https://github.com/dloss/python-pentest-tools)
* [awesome-python - curated list of awesome Python frameworks, libraries and software](https://github.com/vinta/awesome-python)
* [one-python - best Python libraries](https://github.com/geekan/one-python)

### Resources
* https://www.python.org/
* http://learnpythonthehardway.org/book/
* http://www.codecademy.com/en/tracks/python
* http://www.diveintopython.net/
* https://github.com/kennethreitz/python-guide
* http://www.pyvideo.org/speaker/138/raymond-hettinger
* https://github.com/s16h/py-must-watch
* http://pymust.watch/
* http://slides.com/fwkz/awesome-python
* http://docs.python-guide.org/en/latest/
* https://github.com/bslatkin/effectivepython
* https://github.com/kennethreitz/python-guide
* https://github.com/Junnplus/awesome-python-books
* https://github.com/crazyguitar/pysheeet
* https://github.com/satwikkansal/wtfpython
* https://mail.python.org/pipermail/python-list/1999-June/001951.html
* https://github.com/trekhleb/learn-python
* https://docs.python-guide.org/writing/style/
* https://realpython.com/
* https://python-for-system-administrators.readthedocs.io/en/latest/

### Videos
* [Transforming code into beautiful, idiomatic Python](https://www.youtube.com/watch?v=OSGv2VnC0go)

### Books
* [Effective Python](http://www.effectivepython.com/)

### License
MIT
