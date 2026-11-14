from validations.input_schemas import sales_schema, product_schema

def validate_inputs(products, sales):
    products = product_schema.validate(products)
    sales = sales_schema.validate(sales)
    return products, sales
