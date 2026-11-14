import pandera as pa
from pandera import Column, DataFrameSchema

sales_schema = DataFrameSchema({
    "sales id": Column(int),
    "proDuct Id": Column(int),
    "Region": Column(str, nullable=True),
    "qty": Column(int, pa.Check.ge(1)),
    "Price": Column(float),
    "Time stamp": Column(str),
    "discount": Column(float),
    "order_status": Column(str)
})

product_schema = DataFrameSchema({
    "product_id": Column(int),
    "category": Column(str),
    "brand": Column(str),
    "rating": Column(float),
    "in_stock": Column(bool),
    "launch_date": Column(str, nullable=True)
})
