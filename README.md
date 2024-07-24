# CRUDLIB
CRUD Python library using SQLAlchemy ORM

# FOLDER STRUCTURE
```
crudlib/
├── crudlib/
│   ├── __init__.py
│   ├── models.py
│   ├── database.py
│   ├── core.py
├── tests/
│   ├── __init__.py
│   ├── test_crud.py
├── logs/
│   └── log_Y_m_d.log
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

# SETUP
### 1. Update models.py by adding your tables like the User example
* You can use this [link](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html) as reference

# HOWTO
### 1. Create new entry (CREATE)
```python
from crudlib.core import CRUD; crud = CRUD()

tablename = "users"
data = {"name": "User1", "email": "user_sample_1@example.com"}

entry = crud.create_entry(tablename=tablename, data=data)

print(f"name: {entry.name}, email: {entry.email}, inserted: {entry.inserted}")
```

### 2. Read entries (READ)
```python
from crudlib.core import CRUD; crud = CRUD()

tablename = "users"
filters = {"email": "user_sample_1@example.com"}

entries = crud.read_data(tablename=tablename, filters=filters)

for entry in entries:
    print(f"name: {entry.name}, email: {entry.email}, inserted: {entry.inserted}, updated: {entry.updated}")
```

### 3. Update entries (UPDATE)
```python
from crudlib.core import CRUD; crud = CRUD()

tablename = "users"
data = {"name": "User Sample"}
filters = {"email": "user_sample_1@example.com"}

entries = crud.update_data(tablename="users", data=data, filters=filters)

for entry in entries:
    print(f"name: {entry.name}, email: {entry.email}, updated: {entry.updated}")
```

### 4. Delete entry (DELETE)
```python
from crudlib.core import CRUD; crud = CRUD()

tablename = "users"
filters = {"email": "user_sample_1@example.com"}

deleted = crud.delete_data(tablename, filters=filters)

if deleted == 1:
    print("Entry deleted")
else:
    print("Failed to delete entry. Check logs")

```

### 5. Read ALL entries (READ)
```python
from crudlib.core import CRUD; crud = CRUD()

tablename = "users"
filters = {}

entries = crud.read_data(tablename=tablename, filters=filters)

for entry in entries:
    print(f"name: {entry.name}, email: {entry.email}, inserted: {entry.inserted}, updated: {entry.updated}")
```