import io
import json
import os
from setuptools import setup, find_packages


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=find_packages(include=[package_name, package_name + ".*"]),
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    #url='https://github.com/plotly/dash-vtk',
    url='https://github.com/VilhelmC/dash-vtk2',
    install_requires=['dash', 'vtk'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Database :: Front-Ends',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
