import pandas as pd
from pathlib import Path

# =====================================
# Configuración
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_ROOT / "data"

FILES = {
    "Customers": DATA_FOLDER / "Customers.xlsx",
    "Products": DATA_FOLDER / "Products.xlsx",
    "Sellers": DATA_FOLDER / "Sellers.xlsx",
    "Calendar": DATA_FOLDER / "Calendar.xlsx",
    "FactSales": DATA_FOLDER / "FactSales.xlsx"
}

# =====================================
# Leer archivos
# =====================================

customers = pd.read_excel(FILES["Customers"])
products = pd.read_excel(FILES["Products"])
sellers = pd.read_excel(FILES["Sellers"])
calendar = pd.read_excel(FILES["Calendar"])
sales = pd.read_excel(FILES["FactSales"])

print("\n" + "=" * 60)
print("VALIDACIÓN DEL DATASET")
print("=" * 60)

# =====================================
# Cantidad de registros
# =====================================

print("\n1. CANTIDAD DE REGISTROS")

tables = {
    "Customers": customers,
    "Products": products,
    "Sellers": sellers,
    "Calendar": calendar,
    "FactSales": sales
}

for name, df in tables.items():
    print(f"{name:<15}: {len(df):>10,}")

# =====================================
# Valores nulos
# =====================================

print("\n2. VALORES NULOS")

for name, df in tables.items():

    nulls = df.isnull().sum().sum()

    if nulls == 0:
        print(f"✅ {name:<15}: Sin valores nulos")
    else:
        print(f"❌ {name:<15}: {nulls} valores nulos")

# =====================================
# Duplicados
# =====================================

print("\n3. DUPLICADOS")

duplicates = {
    "Customers": customers["CustomerKey"].duplicated().sum(),
    "Products": products["ProductKey"].duplicated().sum(),
    "Sellers": sellers["SellerKey"].duplicated().sum(),
    "Calendar": calendar["DateKey"].duplicated().sum(),
    "FactSales": sales["SaleID"].duplicated().sum()
}

for table, total in duplicates.items():

    if total == 0:
        print(f"✅ {table:<15}: Sin duplicados")
    else:
        print(f"❌ {table:<15}: {total} duplicados")

# =====================================
# Integridad Referencial
# =====================================

print("\n4. INTEGRIDAD REFERENCIAL")

checks = [
    (
        "CustomerKey",
        sales["CustomerKey"],
        customers["CustomerKey"]
    ),
    (
        "ProductKey",
        sales["ProductKey"],
        products["ProductKey"]
    ),
    (
        "SellerKey",
        sales["SellerKey"],
        sellers["SellerKey"]
    ),
    (
        "DateKey",
        sales["DateKey"],
        calendar["DateKey"]
    )
]

for key, fact, dim in checks:

    missing = (~fact.isin(dim)).sum()

    if missing == 0:
        print(f"✅ {key:<15}: OK")
    else:
        print(f"❌ {key:<15}: {missing} registros inválidos")

# =====================================
# Validación de negocio
# =====================================

print("\n5. REGLAS DE NEGOCIO")

negative_sales = (sales["Sales"] <= 0).sum()

negative_profit = (sales["Profit"] < 0).sum()

if negative_sales == 0:
    print("✅ No existen ventas negativas")
else:
    print(f"❌ {negative_sales} ventas negativas")

print(f"ℹ️ Registros con utilidad negativa: {negative_profit:,}")

# =====================================
# Estadísticas
# =====================================

print("\n6. ESTADÍSTICAS")

print(f"Ventas Totales : ${sales['Sales'].sum():,.2f}")
print(f"Costo Total    : ${sales['Cost'].sum():,.2f}")
print(f"Utilidad Total : ${sales['Profit'].sum():,.2f}")

margin = (
    sales["Profit"].sum()
    /
    sales["Sales"].sum()
) * 100

print(f"Margen         : {margin:.2f}%")

print("\n" + "=" * 60)
print("VALIDACIÓN FINALIZADA")
print("=" * 60)
