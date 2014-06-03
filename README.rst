Dropbox Files
=============

A simple dropbox client wrapper for downloading/uploading files.
Requires `Dropbox Python SDK <https://www.dropbox.com/developers/core/sdks/python>`_


Installation
------------

::

    $ pip install git+git


Usage Sample
------------

.. code:: python

    # Initialization
    from dropbox_files import DropboxFiles
    dropbox = DropboxFiles('/path/to/dropbox_token')

    # Download 'somefile.txt' into current directory
    dropbox.download('somefile.txt')

    # Upload 'somefile.txt' to Dropbox's path: '/dropbox_path/somefile.txt'
    dropbox.upload('somefile.txt', '/dropbox_path/')
