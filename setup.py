from setuptools import find_packages, setup

PKG = 'fluffy'

PKG_VERSION = '0.0.1'

setup(
    name=PKG,
    version=PKG_VERSION,
    description=f'The Template',
    packages=find_packages(),
    zip_safe=True,
    setup_requires=['pytest-runner', 'flake8', 'zipp'],
    tests_require=['pytest'],
    entry_points=f"""
        [console_scripts]
        {PKG}={PKG}:main
        """
    )
