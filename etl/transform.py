import pandas as pd

def transform(products, sales):
    sales["Region"] = sales["Region"].str.upper().fillna("UNKNOWN")
    sales["Price"] = sales["Price"].apply(lambda x: max(x, 0))
    sales["Time stamp"] = pd.to_datetime(sales["Time stamp"], errors="coerce")

    df = sales.merge(
        products,
        left_on="proDuct Id",
        right_on="product_id",
        how="left"
    )
    return df
