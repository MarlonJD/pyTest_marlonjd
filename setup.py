from distutils.core import setup
import setuptools
VERSION = "0.0.2"
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()
setup(
    name='pyTest_marlonjd',         # How you named your package folder (MyLib)
    packages=['pyTest_marlonjd'],   # Chose the same as "name"
    # Start with a small number and increase it with every change you make
    version=VERSION,
    license='MIT',
    # Give a short description about your library
    description='PyPi icin deneme paketi',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Burak Karahan',
    author_email='burak.karahan@mail.ru',
    # Provide either the link to your github or to your website
    url='https://github.com/marlonjd/pyTest_marlonjd',
    # I explain this later on
    download_url=f'https://github.com/marlonjd/pyTest_marlonjd/archive/v{VERSION}.tar.gz',
    # Keywords that define your package best
    keywords=['pyTest', 'test'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
