data = {
    "date_key": [140102, 140102, 140102, 140102, 140103, 140103, 140103, 140103],
    "product_sk": [69, 69, 69, 74, 31, 31, 31, 31],
    "store_sk": [4, 5, 5, 3, 2, 3, 3, 8],
    "promotion_sk": [None, 19, None, 23, None, None, 21, None],
    "customer_sk": [None, None, 191, 202, None, None, 123, 233],
    "quantity": [1, 3, 1, 5, 1, 3, 1, 1],
    "net_price": [13.99, 14.99, 14.99, 0.99, 2.49, 14.99, 49.99, 0.99],
    "discount_price": [13.99, 9.99, 14.99, 0.89, 2.49, 9.99, 39.99, 0.99],
}

for key, value in data.items():
    print(key, value[5])

# Bitmap Encoding

import pandas as pd

product_sk = [69, 69, 69, 69, 74, 31, 31, 31, 31, 29, 30, 30, 31, 31, 31, 68, 69, 69]

k = len(set(product_sk))
n = len(product_sk)

bitmap = [[0]*n for _ in range(k)]

index = list(set(product_sk))

df = pd.DataFrame(
    bitmap,
    index=index,
)

for i, product_id in enumerate(product_sk):
    df.loc[product_id, i] = 1

df.columns = product_sk

df.index = [f'product_sk = {idx}' for idx in index]

print(df)
