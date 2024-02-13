from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session, select
import __main__


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


data_connection_str = "postgresql://ahmedmujtaba1:1bKOzMiEgQV9@ep-noisy-surf-36032677.us-east-2.aws.neon.tech/table2?sslmode=require"
engine = create_engine(data_connection_str, echo=True) #echo ---> development

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_hero():
    hero1 = Hero(name="Ahmed Mujtaba", secret_name="AM", age=13)
    hero2 = Hero(name="Saad Mohsin", secret_name="SM")
    hero3 = Hero(name="Mustafa Mohsin", secret_name="MM")
    session = Session(engine)
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()
    session.close()

def get_hero(): # Get
    session = Session(engine)
    statement = select(Hero).where(Hero.name == "Ahmed Mujtaba")
    result = session.exec(statement)
    print(result.all())
    session.commit()
    session.close()

def update_hero(): # Update
    session = Session(engine)
    statement = select(Hero).where(Hero.name == "Ahmed Mujtaba")
    result = session.exec(statement)
    hero = result.one()
    hero.age = 14
    session.add(hero)
    session.commit()
    session.close()

def delete_hero(): # Delete
    session = Session(engine)
    statement = select(Hero).where(Hero.name == "Ahmed Mujtaba")
    result = session.exec(statement)
    hero = result.one()
    session.delete(hero)
    session.commit()
    session.close()

if __name__ == "__main__":
    # create_db_and_tables()
    # create_hero()
    # get_hero()
    update_hero()