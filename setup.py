from setuptools import setup

setup(
    name='pygi',
    version='1.0.3',
    description='Command line interface using gitignore.io API',
    url='http://github.com/onlined/pygi',
    author='Ekin Dursun',
    author_email='ekindursun@gmail.com',
    license='GPLv3',
    py_modules=['pygi'],
    install_requires=[
        'python-Levenshtein',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    entry_points = {
        'console_scripts': ['gi=pygi:main'],
    }
)
