from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class ProductDB(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    quantity = Column(Integer)

    sales = relationship(
    "SaleDB",
    back_populates="product"
    )

class UserDB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True)

    password = Column(String)

class SaleDB(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity_sold = Column(Integer)
    
    product = relationship(
    "ProductDB",
    back_populates="sales"
    )