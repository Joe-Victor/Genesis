from setuptools import setup

setup(
    name='Genesis',
    version='0.0.1',
    description='I HAVE NEEDS',
    url='https://github.com/YoussefV/Genesis',
    author='J',
    license='BSD 2-clause',
    packages=['Genesis'],
    install_requires=['pandas',
                      'numpy<1.21.0',
                      'matplotlib',
                      'IPython',
                      'ipywidgets'],

    classifiers=[
        'Development Status :: 1 - Fucking around',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

