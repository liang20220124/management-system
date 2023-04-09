from sqlalchemy.orm import Session

from . import models

def get_user(db: Session, user_id: str):
    return db.query(models.Member).filter(models.Member.Name == user_id).first()
# if __name__ == '__main__':
#     get_user()