import json
from flask import request
from config import app
from models import Order, User, Offer
from service import init_db, get_all, get_all_by_id, insert_data_user, update_uni, insert_data_offer, insert_data_order, \
    delete_uni


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(response=json.dumps(get_all(User)),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user(request.json)
        return app.response_class(response=json.dumps(request.json),
                                  status=200,
                                  mimetype='application/json'
                                  )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_users_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(User, user_id)
        return app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'PUT':
        update_uni(User, user_id, request.json)
        return app.response_class(response=json.dumps(['Данные успешно обновлены']),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'DELETE':
        delete_uni(User, user_id)
        return app.response_class(response=json.dumps(['Данные успешно обновлены']),
                                  status=200,
                                  mimetype='application/json'
                                  )


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(response=json.dumps(get_all(Order)),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order(request.json)
        return app.response_class(response=json.dumps(request.json),
                                  status=200,
                                  mimetype='application/json'
                                  )


@app.route("/orders/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_orders_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Order, user_id)
        return app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'PUT':
        update_uni(Order, user_id, request.json)
        return app.response_class(response=json.dumps(['Данные успешно обновлены']),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'DELETE':
        delete_uni(Order, user_id)
        return app.response_class(response=json.dumps(['Данные успешно обновлены']),
                                  status=200,
                                  mimetype='application/json'
                                  )


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(response=json.dumps(get_all(Offer)),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer(request.json)
        return app.response_class(response=json.dumps(request.json),
                                  status=200,
                                  mimetype='application/json'
                                  )


@app.route("/offers/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offers_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Offer, user_id)
        return app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'PUT':
        update_uni(Offer, user_id, request.json)
        return app.response_class(response=json.dumps(['Данные успешно обновлены']),
                                  status=200,
                                  mimetype='application/json'
                                  )
    elif request.method == 'DELETE':
        delete_uni(Offer, user_id)
        return app.response_class(response=json.dumps(['Данные успешно обновлены']),
                                  status=200,
                                  mimetype='application/json'
                                  )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
