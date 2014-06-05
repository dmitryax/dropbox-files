Dropbox Files
=============

A simple dropbox client wrapper for downloading/uploading files.

Requires `Dropbox Python SDK <https://www.dropbox.com/developers/core/sdks/python>`_


Installation
------------

::

    $ pip install -e git+https://github.com/hmbg/dropbox-files#egg=dropbox_files


Usage Sample
------------

.. code:: python

    # Initialization
    from dropbox_files import DropboxFiles
    dropbox = DropboxFiles('/path/to/access_token')

    # Download 'somefile.txt' from Dropbox app's root path into current directory
    dropbox.download('somefile.txt')

    # Upload 'somefile.txt' to Dropbox app's path: '/dropbox_path/somefile.txt'
    dropbox.upload('somefile.txt', '/dropbox_path/')
