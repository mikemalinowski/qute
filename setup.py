import os
import setuptools

short_description = 'A Qt.py extension which aims to expose additional helper utilities to Qt which are common place within coding projects.'
if os.path.exists('README.md'):
    with open('README.md', 'r') as fh:
        long_description = fh.read()

else:
    long_description = short_description

setuptools.setup(
    name='qute',
    version='1.0.10',
    author='Mike Malinowski',
    author_email='mike@twisted.space',
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/qute',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_data={
        '': ['styles/*.css', '_res/*.png'],
    },
    keywords="qute qt pyside pyside2 pyqt",
)
