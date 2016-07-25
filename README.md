# pygi 

Command line interface using gitignore.io API

## Installation:

```
# pip install pygi
```
## Usage:

```
$ gi --list
actionscript
ada
agda
...
yii2
zendframework
zephir
$ gi vim werckercli > .gitignore
$ cat .gitignore

### Vim ###
# swap
[._]*.s[a-w][a-z]
[._]s[a-w][a-z]
# session
Session.vim
# temporary
.netrwhist
*~
# auto-generated tag files
tags


### WerckerCLI ###
_steps
_builds
_cache
_projects

```

**pygi** also can be used as a library too:
```python
>>> import pygi
>>> gitignores = pygi.list()
>>> len(gitignores)
290
>>> gitignores[4]
'android'
>>> print(pygi.gitignores('vim', 'werckercli'))

### Vim ###
# swap
[._]*.s[a-w][a-z]
[._]s[a-w][a-z]
# session
Session.vim
# temporary
.netrwhist
*~
# auto-generated tag files
tags


### WerckerCLI ###
_steps
_builds
_cache
_projects

```





