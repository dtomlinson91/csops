# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['csops']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['csops = csops.run:run']}

setup_kwargs = {
    'name': 'csops',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Daniel Tomlinson',
    'author_email': 'dtomlinson@panaetius.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
