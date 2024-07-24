# CRUDLIB
CRUD Python library using SQLAlchemy ORM

# FOLDER STRUCTURE
```
crud_library/
├── crud/
│   ├── __init__.py
│   ├── models.py
│   ├── database.py
│   ├── crud_operations.py
├── tests/
│   ├── __init__.py
│   ├── test_crud_operations.py
├── logs/
│   └── app.log
├── README.md
├── setup.py
├── requirements.txt
├── dev.env # You have to create this file
```

# INSTALLATION
### 1. Clone crudlib repo
```git clone https://github.com/porfyriosg/pgnlp.git```
### 2. Export crudlib repo file path
```export CRUDENV=$HOME/crudlib```
### 3. Remove ".sample" from "dev.env.sample"
```mv dev.env.sample dev.env```
### 4. Create environment
```python -m venv .venv```
### 5. Activate environment
```source .venv/bin/activate```
### 6. Install requirements.txt
```pip install -r requirements.txt```
### 7. Install crudlib
```pip install -U .```