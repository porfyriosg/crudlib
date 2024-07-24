from setuptools import setup, find_packages

setup(
    name="crudlib",
    version="0.1.4",
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