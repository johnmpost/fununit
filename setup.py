from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='fununit',
    version='1.0.0',
    description='a functional, declarative, unit-testing library for testing pure functions',
    long_description=long_description,
    author='John Post',
    author_email='muffinpost1@gmail.com',
    url='https://github.com/johnmpost/fununit',
    license='WTFPL',
    classifiers=[
        'License :: WTFPL',
        'License :: Freely Distributable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Unit',
    ],
    keywords=['unit testing', 'testing', 'functional', 'declarative', 'pure functions', 'testing boilerplate'],
    python_requires='>=3.9',
    install_requires=[],
    scripts=[],
)
