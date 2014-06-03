from setuptools import setup


setup(
    name='dropbox_files',
    version=open('VERSION').read().strip(),
    description='Simple Dropbox wrapper for downloading/uploading files',
    long_description=open('README.rst').read(),

    author='Dmitry Anoshin',
    author_email='anoshindx@gmail.com',

    license='MIT License',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='dropbox wrapper',

    py_modules=['dropbox_files'],

    install_requires=['dropbox',],
)