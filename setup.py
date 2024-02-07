from setuptools import setup, find_packages

setup(
    name='pyfetch',
    version='1.0.0',
    description='A command-line tool to fetch data based on request files.',
    author='Enock Zaake',
    author_email='zaakeenock@example.com',
    packages=find_packages(),
    install_requires=[
        'certifi==2024.2.2',
        'charset-normalizer==3.3.2',
        'colorama==0.4.6',
        'idna==3.6',
        'iniconfig==2.0.0',
        'packaging==23.2',
        'pluggy==1.4.0',
        'pytest==8.0.0',
        'PyYAML==6.0.1',
        'requests==2.31.0',
        'setuptools==69.0.3',
        'typing==3.7.4.3',
        'urllib3==2.2.0',
    ],
    entry_points={
        'console_scripts': [
            'pyfetch = pyfetch.__main__:main',
        ],
    },
)
