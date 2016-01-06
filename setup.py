from setuptools import setup

setup(
    name='tamproxy',
    version='0.0.4',

    description='TAMProxy Python Host',
    url='https://github.com/mitchgu/TAMProxy-pyHost',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='maslab tamproxy',
    packages=['tamproxy'],
    install_requires=['six', 'numpy', 'pyserial>=3.0', 'PyYAML'],
)
