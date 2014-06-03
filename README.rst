Dropbox Files
=============

A simple dropbox client wrapper for downloading/uploading files.

Requires `Dropbox Python SDK <https://www.dropbox.com/developers/core/sdks/python>`_


Installation
------------

::

    $ pip install git+https://github.com/hmbg/dropbox-files


Usage Sample
------------

.. code:: python

    # Initialization
    from dropbox_files import DropboxFiles
    dropbox = DropboxFiles('/path/to/dropbox_token')

    # Download from Dropbox app's root path 'somefile.txt' into current directory
    dropbox.download('somefile.txt')

    # Upload 'somefile.txt' to Dropbox app's path: '/dropbox_path/somefile.txt'
    dropbox.upload('somefile.txt', '/dropbox_path/')
