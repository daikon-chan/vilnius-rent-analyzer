import pandas as pd

df = pd.read_csv("data/raw/housing_sample.csv")

print("先頭5件")
print(df.head())

print("\n列名一覧")
print(df.columns.tolist())

print("\nデータ型")
print(df.dtypes)

print("\n件数")
print(len(df))

print("\n平均家賃")
print(df["price_eur"].mean())