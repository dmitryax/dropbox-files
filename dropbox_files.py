import os.path
import posixpath

from dropbox.client import DropboxClient
from dropbox.rest import ErrorResponse


class DropboxFiles():

    """Simple class for downloading/uploading files from/upto Dropbox

    It requires an already generated access_token which can be provided
    as a string or as a local filepath to the file containing one
    """

    class TokenNotProvidedError():
        pass

    def __init__(self, filepath=None, token=None):
        if not (filepath or token):
            raise TokenNotProvidedError('Access token is not provided')

        if filepath:
            with open(filepath) as token_file:
                token = token_file.read().strip()

        self.client = DropboxClient(token)


    def download(self, dropbox_filepath, local_filepath=None):
        """
        If there is a file at Dropbox with the given `dropbox_filepath`
        the function returns a filepath of downloaded file
        otherwise it returns `None`
        """

        filename = posixpath.basename(dropbox_filepath)
        if not local_filepath:
            local_filepath = filename
        if os.path.isdir(local_filepath):
            local_filepath = os.path.join(local_filepath, filename)

        try:
            with self.client.get_file(dropbox_filepath) as dropbox_file, \
                 open(local_filepath, 'wb') as local_file:
                local_file.write(dropbox_file.read())
        except ErrorResponse as e:
            if e.status == 404:
                return None
            else:
                raise

        return local_filepath


    def upload(self, local_filepath, dropbox_filepath=None):
        filename = os.path.basename(local_filepath)
        if not dropbox_filepath:
            dropbox_filepath = posixpath.join('/', filename)
        if dropbox_filepath.endswith('/'): # dropbox_filepath is a dir
            dropbox_filepath = posixpath.join(dropbox_filepath, filename)

        with open(local_filepath, 'rb') as local_file:
            self.client.put_file(dropbox_filepath, local_file, overwrite=True)