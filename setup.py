from setuptools import setup

setup(
    name='dndbeyond_websearch',
    version='0.2',
    packages=['dndbeyond_websearch'],
    install_requires=['requests', 'beautifulsoup4'],
    url='https://github.com/VadimPushtaev/dndbeyond_websearch',
    license='MIT',
    author='Vadim Pushtaev',
    author_email='pushtaev.vm@gmail.com',
    description='Search via dndbeyond.com built-in search'
)
