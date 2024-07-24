from setuptools import setup, find_packages
from crudlib import __version__

setup(
    name="crudlib",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy",
        "python-dotenv"
    ],
    # entry_points={
    #     'console_scripts': [
    #         'crud_library=crud_library.__main__:main',
    #     ],
    # },
)