import json

from models import *
from config import db


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get('id'),
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                age=row.get('age'),
                email=row.get('email'),
                role=row.get('role'),
                phone=row.get('phone')
            )
        )
    db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get('id'),
                name=row.get('name'),
                description=row.get('description'),
                start_data=row.get('start_data'),
                end_data=row.get('end_data'),
                address=row.get('address'),
                price=row.get('price'),
                customer_id=row.get('customer_id'),
                executor_id=row.get('executor_id')
            )
        )

    db.session.commit()


def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get('id'),
                order_id=row.get('order_id'),
                executor_id=row.get('executor_id')
            )
        )
    db.session.commit()


def get_all(model):
    """ Получение информации по модулю """
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result


def get_all_by_id(model, user_id):
    """ Получения id по модулю """
    try:
        return db.session.query(model).get(user_id).to_dict()
    except Exception:
        return {}


def update_uni(model, user_id, values):
    """ Обновляет данные по модулю"""
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception:
        return {}


def delete_uni(model, user_id):
    """ Обновляет данные по модулю"""
    try:
        db.session.query(model).filter(model.id == user_id).delete
        db.session.commit()
    except Exception:
        return {}



def init_db():
    """Инициализирует базу данных"""
    db.drop_all()
    db.create_all()
    with open('data/user.json',  encoding="utf-8") as file:
        insert_data_user(json.load(file))

    with open('data/orders.json',  encoding="utf-8") as file:
        insert_data_order(json.load(file))

    with open('data/offers.json',  encoding="utf-8") as file:
        insert_data_offer(json.load(file))
