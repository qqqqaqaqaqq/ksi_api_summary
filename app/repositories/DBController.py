# sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# 시스템
from datetime import datetime, timezone
from psycopg2 import IntegrityError

# 앱 내부
from app.db.session import SessionLocal

from app.core.settings import settings

# 암호화
from cryptography.fernet import Fernet

cipher = Fernet(settings.FERNET_KEY.encode())

def trade_insert(userid:str, data:dict):
    db = SessionLocal()
    try:

        db.commit()            
    except SQLAlchemyError as e:
        db.rollback()
        print("DB 오류:", e)
    except Exception as e:
        db.rollback()
        print("알 수 없는 오류:", e)
    finally:
        db.close()
