from setuptools import setup, find_packages

setup(
    name='remotedatasync',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'remotedatasync = remotedatasync.main:main'
        ]
    },
    author='Oliver Wójcik',
    description='Pakiet do pobierania i wystawiania danych z API',
    python_requires='>=3.7',
)
