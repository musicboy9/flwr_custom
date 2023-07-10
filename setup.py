from setuptools import setup, find_packages

setup(
    name                = 'flwr_custom',
    version             = '0.1.2',
    description         = 'custom flwr 1.4.0 for fl viewer',
    author              = 'ymkoh',
    author_email        = 'musicboy9@snu.ac.kr',
    url                 = 'https://github.com/musicboy9/flwr_custom',
    download_url        = 'https://github.com/musicboy9/flwr_custom/archive/refs/heads/feature/1-AddLibrary.zip',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['flwr_custom'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)