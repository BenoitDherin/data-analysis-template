website
=======

Source for generating website using pelican

Installation
============

It's best to install in a virtualenv because you need a specific version of
IPython, in particualar.  Something like::

    virtualenv pelican-blog
    . pelican-blog/bin/activate
    pip install -r requirements.txt

Developing
==========

To run Pelican in regeneration mode and serve the output at
http://localhost:8000, type:

    make devserver

Once you are happy with your changes, type::

    make stopserver

Publishing
==========

To build the site and push it to github, type:

    make github

The updated page can be viewed here: http://berkeley-stat133.github.io/

Cleaning up
===========

When you've finished working on the blog, deactivate the virtualenv::

    deactivate

To start working on it again, ``cd`` into this directory and::

    . pelican-blog/bin/activate
