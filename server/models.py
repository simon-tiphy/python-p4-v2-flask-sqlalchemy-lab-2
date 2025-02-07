
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy_serializer import SerializerMixin


# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })

# db = SQLAlchemy(metadata=metadata)


# class Customer(db.Model, SerializerMixin):
#     __tablename__ = 'customers'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)

#     # Relationship to Review (One to Many)
#     reviews = db.relationship('Review', back_populates='customer', lazy=True)

#     # Association Proxy for Items
#     items = association_proxy('reviews', 'item')

#     def __repr__(self):
#         return f'<Customer {self.id}, {self.name}>'


# class Item(db.Model, SerializerMixin):
#     __tablename__ = 'items'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     price = db.Column(db.Float)

#     # Relationship to Review (One to Many)
#     reviews = db.relationship('Review', back_populates='item', lazy=True)

#     def __repr__(self):
#         return f'<Item {self.id}, {self.name}, {self.price}>'


# class Review(db.Model):
#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.String)

#     # Foreign Keys
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
#     item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

#     # Relationships to Customer and Item
#     customer = db.relationship('Customer', back_populates='reviews')
#     item = db.relationship('Item', back_populates='reviews')

#     def __repr__(self):
#         return f'<Review {self.id}, {self.comment}, {self.customer_id}, {self.item_id}>'

#     # SerializerMixin Exclusions to avoid recursion
#     def to_dict(self):
#         data = super().to_dict()
#         data.pop('customer', None)  # Exclude customer from serialized review
#         data.pop('item', None)  # Exclude item from serialized review
#         return data



from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Relationship to Review
    reviews = db.relationship('Review', back_populates='customer')
    # Association proxy for items through reviews
    items = association_proxy('reviews', 'item')

    serialize_rules = ('-reviews.customer',)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    # Relationship to Review
    reviews = db.relationship('Review', back_populates='item')

    serialize_rules = ('-reviews.item',)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    # Relationships to Customer and Item
    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')

    serialize_rules = ('-customer.reviews', '-item.reviews')

    def __repr__(self):
        return f'<Review {self.id}, {self.comment}, Customer {self.customer_id}, Item {self.item_id}>'