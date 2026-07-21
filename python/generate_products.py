import pandas as pd
import random
from pathlib import Path

# ---------------------------------
# Configuración
# ---------------------------------

random.seed(123)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_ROOT / "data"
DATA_FOLDER.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_FOLDER / "Products.xlsx"

# ---------------------------------
# Catálogo de productos
# ---------------------------------

catalog = {
    "Tecnología": {
        "Laptop": [
            "Dell", "HP", "Lenovo", "Asus", "Acer"
        ],
        "Monitor": [
            "Samsung", "LG", "Dell", "AOC"
        ],
        "Impresora": [
            "HP", "Epson", "Canon", "Brother"
        ],
        "Accesorios": [
            "Logitech", "Microsoft", "Genius", "Kingston"
        ]
    },

    "Muebles": {
        "Escritorio": [
            "OfficePro", "IKEA", "HomeCenter"
        ],
        "Silla": [
            "OfficePro", "IKEA", "Steelcase"
        ],
        "Archivador": [
            "OfficePro", "MetalWorks"
        ]
    },

    "Oficina": {
        "Papelería": [
            "Bic", "Faber Castell", "Pilot"
        ],
        "Cuadernos": [
            "Norma", "Oxford"
        ],
        "Organizadores": [
            "OfficePro", "3M"
        ]
    }
}

colors = [
    "Negro",
    "Blanco",
    "Gris",
    "Azul",
    "Rojo",
    "Verde",
    "Plateado"
]

# ---------------------------------
# Crear productos
# ---------------------------------

products = []

product_key = 1

while product_key <= 500:

    category = random.choice(list(catalog.keys()))

    subcategory = random.choice(
        list(catalog[category].keys())
    )

    brand = random.choice(
        catalog[category][subcategory]
    )

    color = random.choice(colors)

    cost = round(
        random.uniform(5, 1200),
        2
    )

    margin = random.uniform(
        1.15,
        1.60
    )

    unit_price = round(
        cost * margin,
        2
    )

    product_name = f"{brand} {subcategory} {product_key}"

    products.append({

        "ProductKey": product_key,

        "ProductID": f"PROD-{product_key:04}",

        "ProductName": product_name,

        "Category": category,

        "SubCategory": subcategory,

        "Brand": brand,

        "Color": color,

        "Cost": cost,

        "UnitPrice": unit_price

    })

    product_key += 1

# ---------------------------------
# Crear DataFrame
# ---------------------------------

df = pd.DataFrame(products)

df.to_excel(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("DimProducts creada correctamente")
print(f"Archivo: {OUTPUT_FILE}")
print(f"Registros: {len(df):,}")
print("=" * 50)
