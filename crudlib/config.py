import os
import datetime
import logging
from dotenv import load_dotenv

__ENV__ = os.getenv("CRUDENV")
__ENVFILE__ = os.path.join(__ENV__, "dev.env")
load_dotenv(__ENVFILE__)

__LOGS__ = os.path.join(__ENV__, "logs")
__TESTS__ = os.path.join(__ENV__, "tests")

__TODAY_TAG__ = datetime.datetime.now().strftime("%Y_%m_%d")

__LOGFILE__ = os.path.join(__LOGS__, f'log_{__TODAY_TAG__}.log')
logging.basicConfig(filename=__LOGFILE__, level=logging.INFO)

class Config:

    @staticmethod
    def get_db_url():
        db_url = os.getenv("DATABASE_URL")
        if "sqlite" in db_url:
            db_name = db_url.replace("sqlite:///", "")
            db_path = os.path.join(__ENV__, db_name)
            db_url = f"sqlite:///{db_path}"
        
        return db_url
    
