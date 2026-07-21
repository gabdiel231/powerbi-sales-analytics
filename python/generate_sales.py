import pandas as pd
import numpy as np
import random
from pathlib import Path

# ---------------------------------
# Configuración
# ---------------------------------

random.seed(123)
np.random.seed(123)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_ROOT / "data"

CUSTOMERS_FILE = DATA_FOLDER / "Customers.xlsx"
PRODUCTS_FILE = DATA_FOLDER / "Products.xlsx"
SELLERS_FILE = DATA_FOLDER / "Sellers.xlsx"
CALENDAR_FILE = DATA_FOLDER / "Calendar.xlsx"

OUTPUT_FILE = DATA_FOLDER / "FactSales.xlsx"

# ---------------------------------
# Leer dimensiones
# ---------------------------------

customers = pd.read_excel(CUSTOMERS_FILE)
products = pd.read_excel(PRODUCTS_FILE)
sellers = pd.read_excel(SELLERS_FILE)
calendar = pd.read_excel(CALENDAR_FILE)

# ---------------------------------
# Cantidad de ventas
# ---------------------------------

TOTAL_SALES = 100000

sales = []

# ---------------------------------
# Generar ventas
# ---------------------------------

for sale_id in range(1, TOTAL_SALES + 1):

    customer = customers.sample(1).iloc[0]
    product = products.sample(1).iloc[0]
    seller = sellers.sample(1).iloc[0]
    date = calendar.sample(1).iloc[0]

    quantity = random.randint(1, 10)

    unit_price = round(product["UnitPrice"], 2)

    cost = round(product["Cost"], 2)

    discount = random.choice([
        0,
        0,
        0,
        0.05,
        0.10,
        0.15
    ])

    gross_sales = quantity * unit_price

    discount_amount = gross_sales * discount

    sales_amount = gross_sales - discount_amount

    total_cost = quantity * cost

    profit = sales_amount - total_cost

    sales.append({

        "SaleID": sale_id,

        "DateKey": int(date["DateKey"]),

        "CustomerKey": int(customer["CustomerKey"]),

        "ProductKey": int(product["ProductKey"]),

        "SellerKey": int(seller["SellerKey"]),

        "Quantity": quantity,

        "UnitPrice": unit_price,

        "Discount": discount,

        "Sales": round(sales_amount,2),

        "Cost": round(total_cost,2),

        "Profit": round(profit,2)

    })

# ---------------------------------
# Crear DataFrame
# ---------------------------------

df = pd.DataFrame(sales)

# ---------------------------------
# Exportar
# ---------------------------------

df.to_excel(
    OUTPUT_FILE,
    index=False
)

print("="*60)
print("FACT SALES CREADA CORRECTAMENTE")
print("="*60)
print(f"Archivo : {OUTPUT_FILE}")
print(f"Ventas  : {len(df):,}")
print(f"Total Sales : ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print("="*60)
