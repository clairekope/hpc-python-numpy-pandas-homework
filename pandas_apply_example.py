import pandas as pd

company_orders = pd.read_csv("orders.csv")

def discounted_total(order):
    return order["unit_price"] * order["quantity"] * (1 - order["discount"])

company_orders["total"] = company_orders.apply(discounted_total, axis=1)

print(company_orders[["order_id", "total"]].head())