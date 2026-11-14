import pandera as pa
from pandera import Column, DataFrameSchema

output_schema = DataFrameSchema({
    "sales id": Column(int),
    "product_id": Column(int),
    "qty": Column(int, pa.Check.ge(1)),
    "Price": Column(float, pa.Check.ge(0)),
    "category": Column(str),
    "brand": Column(str),
})
