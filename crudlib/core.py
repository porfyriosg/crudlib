from crudlib.database import DB
import logging

class CRUD(DB):

    def __init__(self) -> None:
        super().__init__()

    def create_entry(self, tablename: str, data: dict):
        """
        Creates a new entry in the specified table.

        Args:
            tablename (str): The name of the table.
            data (dict): Data for the new entry.

        Returns:
            db_obj (Base): The created database object.
        """
        entry = self._create(tablename, data)
        return entry

    def read_data(self, tablename: str, filters: dict):
        """
        Reads entries from the specified table based on filters.

        Args:
            tablename (str): The name of the table.
            filters (dict): Filters for the query.

        Returns:
            results (list): List of retrieved entries.
        """

        entries = self._read(tablename, filters)
        return entries

    def update_data(self, tablename: str, filters: dict, data: dict):
        """
        Updates entries in the specified table based on filters.

        Args:
            tablename (str): The name of the table.
            filters (dict): Filters for the query.
            data (dict): Data to update.

        Returns:
            updated (list): List of updated entries.
        """

        entry = self._update(tablename, filters, data)
        return entry

    def delete_data(self, tablename: str, filters: dict):
        """
        Deletes entries from the specified table based on filters.

        Args:
            tablename (str): The name of the table.
            filters (dict): Filters for the query.

        Returns:
            deleted (int): Number of deleted entries.
        """

        deleted = self._delete(tablename, filters)
        return deleted
