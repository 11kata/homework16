from config import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String(100))
    phone = db.Column(db.String)

    def to_dict(self):
        """Перевод данных User в словарь"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role,
            'phone': self.phone
        }


class Order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    start_data = db.Column(db.Integer)
    end_data = db.Column(db.Integer)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def to_dict(self):
        """Перевод данных Order в словарь"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_data': self.start_data,
            'end_data': self.end_data,
            'address': self.address,
            'price': self.price,
            'customer_id': self.customer_id,
            'executor_id': self.executor_id
        }


class Offer(db.Model):
    __tablename__ = 'Offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def to_dict(self):
        """Перевод данных Offer в словарь"""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id
        }
