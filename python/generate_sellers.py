import pandas as pd
import random
from pathlib import Path
from faker import Faker

# ---------------------------------
# Configuración
# ---------------------------------

fake = Faker("es_ES")
random.seed(123)
Faker.seed(123)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_ROOT / "data"
DATA_FOLDER.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_FOLDER / "Sellers.xlsx"

# ---------------------------------
# Catálogos
# ---------------------------------

countries = {
    "Panamá": [
        "Panamá",
        "David",
        "Colón",
        "Santiago"
    ],
    "Costa Rica": [
        "San José",
        "Alajuela",
        "Cartago"
    ],
    "Colombia": [
        "Bogotá",
        "Medellín",
        "Cali"
    ],
    "México": [
        "Ciudad de México",
        "Guadalajara",
        "Monterrey"
    ]
}

departments = [
    "Retail",
    "Corporativo",
    "Mayorista",
    "E-commerce"
]

managers = [
    "Carlos Mendoza",
    "María González",
    "Luis Rodríguez",
    "Ana Torres",
    "José Herrera"
]

# ---------------------------------
# Crear vendedores
# ---------------------------------

sellers = []

for seller_key in range(1, 101):

    country = random.choice(list(countries.keys()))
    city = random.choice(countries[country])

    commission = round(
        random.uniform(0.02, 0.08),
        4
    )

    salary = random.randint(
        900,
        2500
    )

    sellers.append({

        "SellerKey": seller_key,

        "SellerID": f"SELL-{seller_key:03}",

        "SellerName": fake.name(),

        "Country": country,

        "City": city,

        "Department": random.choice(departments),

        "Manager": random.choice(managers),

        "CommissionRate": commission,

        "BaseSalary": salary,

        "HireDate": fake.date_between(
            start_date="-10y",
            end_date="today"
        )

    })

# ---------------------------------
# Crear DataFrame
# ---------------------------------

df = pd.DataFrame(sellers)

df.to_excel(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("DimSellers creada correctamente")
print(f"Archivo: {OUTPUT_FILE}")
print(f"Registros: {len(df):,}")
print("=" * 50)
