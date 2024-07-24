import logging
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from crudlib.config import Config
from crudlib.models import Base

DATABASE_URL = Config.get_db_url()

engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(session_factory)

class DB:
    _db = None
    _timer = None

    def __init__(self) -> None:
        self._make_tables()

    def _make_tables(self):
        try:
            Base.metadata.create_all(engine)
        except Exception as error:
            logging.warning(f"Cannot create tables: {error}")

    def get_model_from_table(self, tablename: str):
        """
        Retrieves a model class by its table name.

        Args:
            tablename (str): The name of the table.

        Returns:
            model (Base): The model class corresponding to the table name.
        """
        for mapper in Base.registry.mappers:
            if mapper.persist_selectable.name == tablename:
                return mapper.class_
            
        logging.error(f"Model {tablename} not found")

    def _create(self, tablename: str, data: dict):
        """
        Creates a new entry in the specified table.

        Args:
            tablename (str): The name of the table.
            data (dict): Data for the new entry.

        Returns:
            db_obj (Base): The created database object.
        """
        model = self.get_model_from_table(tablename)
        try:
            db_obj = model(**data)
            with Session() as db:
                db.add(db_obj)
                db.commit()
                db.refresh(db_obj)
                logging.info(f"CREATED '{tablename}' entry: {data}")
                return db_obj
        except Exception as error:
            logging.warning(f"Cannot CREATE entry for '{tablename}': {error}")

    def _read(self, tablename: str, filters: dict):
        """
        Reads entries from the specified table based on filters.

        Args:
            tablename (str): The name of the table.
            filters (dict): Filters for the query.

        Returns:
            results (list): List of retrieved entries.
        """
        model = self.get_model_from_table(tablename)
        try:
            with Session() as db:
                query = db.query(model)
                for key, value in filters.items():
                    query = query.filter(getattr(model, key) == value)
                results = query.all()
                logging.info(f"READ '{tablename}' entries with filters: {filters}")
        except Exception as error:
            logging.warning(f"Cannot READ entries for '{tablename}': {error}")

        return results

    def _update(self, tablename: str, filters: dict, data: dict):
        """
        Updates entries in the specified table based on filters.

        Args:
            tablename (str): The name of the table.
            filters (dict): Filters for the query.
            data (dict): Data to update.

        Returns:
            updated (list): List of updated entries.
        """
        model = self.get_model_from_table(tablename)
        try:
            with Session() as db:
                query = db.query(model)
                for key, value in filters.items():
                    query = query.filter(getattr(model, key) == value)
                query.update(data)
                db.commit()
                logging.info(f"UPDATED '{tablename}' entries with filters: {filters} and data: {data}")
                return query.all()
            
        except Exception as error:
            logging.warning(f"Cannot UPDATE entry for '{tablename}': {error}")

    def _delete(self, tablename: str, filters: dict):
        """
        Deletes entries from the specified table based on filters.

        Args:
            db (Session): SQLAlchemy session.
            tablename (str): The name of the table.
            filters (dict): Filters for the query.

        Returns:
            deleted (int): Number of deleted entries.
        """
        model = self.get_model_from_table(tablename)
        try:
            with Session() as db:
                query = db.query(model)
                for key, value in filters.items():
                    query = query.filter(getattr(model, key) == value)
                deleted = query.delete()
                db.commit()
                logging.info(f"DELETED {deleted} '{tablename}' entries with filters: {filters}")
                return deleted
        except Exception as error:
            logging.warning(f"Cannot DELETE entry due to: {error}")