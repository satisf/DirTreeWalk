from setuptools import setup

setup(
    name='DirTreeWalk',
    version='0.1',
    py_modules=['DirTreeWalk'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        dtw=DirTreeWalk:cli
    ''',
)