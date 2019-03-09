# Python project sample with sphinx docs and unittest
  

## conf.py in docs 🥑

```
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

extensions = [
'sphinx.ext.autodoc',
'sphinx_tabs.tabs',
'sphinx.ext.napoleon'
]

html_theme = 'sphinx_rtd_theme'
```

## Work flow
```
cd project/docs
sphinx-apidoc -f -o source/ ../src
//this will generate modules.rst and other main.rst etc for each python file into the docs/source diretory

make html

add to your existing index.rst or any other page 
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   source/modules
```