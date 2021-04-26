from setuptools import setup, find_packages

setup(
    name='battery_test_web',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'sqlalchemy_utils',
        'python-dotenv',
    ]
)
