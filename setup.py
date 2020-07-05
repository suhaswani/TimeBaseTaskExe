from setuptools import setup,find_packages
setup(
    name='TbTe',
    version=1.1,
    packages=find_packages(),
    test_suite="test",
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    )

