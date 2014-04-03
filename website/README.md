website
=======

This directory contains the files needed to generate a simple website to 
1. display the iPython data analysis notebooks stored in the directory `../notebooks`
2. push this generated website to the github website associated to your fork of this repository

The website is generated using the [Pelican Static Site Generator](http://blog.getpelican.com/) written in Python. 
You'll find additional documentation on how to modify this static website at the link above to further customize
the default website used here. 

Important
========= 

Before using the website you'll need to modify a few things
in the following configuration files:

* `pelicanconf.py`
* `publishconf.py`
* `Makefile`

### In the file `pelicanconf.py`

Replace the value of variables shown below by the
information corresponding to your project:

```
###################################################
# AUTHORSHIP AND WEBSITE INFO (Replace accordingly)
###################################################
AUTHOR = u'Benoit Dherin'
SITENAME = u'Data Analysis Project'
SITESUBTITLE = u'Template using the iPython notebook'
GITHUB_REPOSITORY_URL = u'https://github.com/BenoitDherin/data-analysis-template'
###################################################
```

### In the file `publishconf.py`

Replace the value of `SITEURL` by the website url associated to your
github repository. (See [here](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)
to find out how to customize this url).

```
####################################################################
# URL of the github repository website associated with the fork
# of this repository  (Replace accordingly)
####################################################################
SITEURL = 'http://benoitdherin.github.io/data-analysis-template'
####################################################################
```

### In the file `Makefile`

```
##################################################################################
# Replace below with the corresponding info for your fork of the github repository 
##################################################################################
GITHUB_REPOSITORY=https://github.com/BenoitDherin/data-analysis-template.git
##################################################################################
```

Generating and Pushing the website
==================================

Once the configuration above have been appropriately modified, you'll be able to generate and push your website using the command

`make github`

(For that command to work, you'll need to be in the same directory where the `Makefile` is located.)




Software requirements
====================

You should not need any further configuration nor software installations, provided you are using
the virutual machine `OskiBox`. You'll find the instructions to construct the machine [here].
It's best to install in a virtualenv because you need a specific version of

Modifying the website
====================

To see what your website will looklike once pushed on github, you can run on your local computer
the following command:

`make devserver`

This will powered on a simple webserver, running your website locally on your computer
at the following url:

`http://localhost:8000`

Don't forget to stop the server, once done with the modifications:

`make stopserver`

