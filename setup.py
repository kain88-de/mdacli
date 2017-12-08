from setuptools import setup

setup(
    name='mdacli',
    version='0.0.1',
    description='mdacli',
    author='Max Linke',
    license='GPL-3',
    packages=['mdacli'],
    install_requires=[
        'mdanalysis',
        'click',
        'panedr',
        'matplotlib',
    ],
    entry_points={'console_scripts': ['mdacli=mdacli.cli:cli']},
    tests_require=['pytest'],
    zip_safe=False)
