from faker import Faker
import pandas as pd
import random
from pathlib import Path

# ---------------------------------
# Configuración
# ---------------------------------

fake = Faker("es_ES")
random.seed(123)
Faker.seed(123)

# Ruta del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Carpeta donde se guardarán los Excel
DATA_FOLDER = PROJECT_ROOT / "data"
DATA_FOLDER.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_FOLDER / "Customers.xlsx"

# ---------------------------------
# Catálogos
# ---------------------------------

countries = {
    "Panamá": [
        "Panamá",
        "San Miguelito",
        "David",
        "Santiago",
        "Colón"
    ],
    "Costa Rica": [
        "San José",
        "Alajuela",
        "Cartago",
        "Heredia",
        "Liberia"
    ],
    "Colombia": [
        "Bogotá",
        "Medellín",
        "Cali",
        "Barranquilla",
        "Cartagena"
    ],
    "México": [
        "Ciudad de México",
        "Guadalajara",
        "Monterrey",
        "Puebla",
        "Querétaro"
    ]
}

segments = [
    "Consumer",
    "Corporate",
    "Home Office"
]

# ---------------------------------
# Crear clientes
# ---------------------------------

customers = []

for customer_id in range(1, 5001):

    country = random.choice(list(countries.keys()))
    city = random.choice(countries[country])

    customers.append({

        "CustomerKey": customer_id,

        "CustomerID": f"CUST-{customer_id:05}",

        "CustomerName": fake.name(),

        "Gender": random.choice([
            "Male",
            "Female"
        ]),

        "Age": random.randint(18, 70),

        "Country": country,

        "City": city,

        "Segment": random.choice(segments),

        "RegistrationDate": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

# ---------------------------------
# DataFrame
# ---------------------------------

df = pd.DataFrame(customers)

df.to_excel(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("DimCustomers creada correctamente")
print(f"Archivo: {OUTPUT_FILE}")
print(f"Registros: {len(df):,}")
print("=" * 50)
