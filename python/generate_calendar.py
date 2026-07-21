import pandas as pd
from pathlib import Path

# ---------------------------------
# Configuración
# ---------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_ROOT / "data"
DATA_FOLDER.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_FOLDER / "Calendar.xlsx"

# ---------------------------------
# Crear calendario
# ---------------------------------

start_date = "2021-01-01"
end_date = "2025-12-31"

calendar = pd.date_range(
    start=start_date,
    end=end_date,
    freq="D"
)

df = pd.DataFrame({
    "Date": calendar
})

# ---------------------------------
# Atributos de fecha
# ---------------------------------

df["DateKey"] = df["Date"].dt.strftime("%Y%m%d").astype(int)

df["Year"] = df["Date"].dt.year

df["Quarter"] = "Q" + df["Date"].dt.quarter.astype(str)

df["MonthNumber"] = df["Date"].dt.month

df["MonthName"] = df["Date"].dt.month_name(locale="es_ES")

df["Week"] = df["Date"].dt.isocalendar().week.astype(int)

df["Day"] = df["Date"].dt.day

df["DayName"] = df["Date"].dt.day_name(locale="es_ES")

df["DayOfYear"] = df["Date"].dt.dayofyear

df["IsWeekend"] = df["Date"].dt.weekday >= 5

df["IsWeekend"] = df["IsWeekend"].map({
    True: "Sí",
    False: "No"
})

df["Semester"] = df["Quarter"].apply(
    lambda x: "S1" if x in ["Q1", "Q2"] else "S2"
)

df["MonthYear"] = df["Date"].dt.strftime("%Y-%m")

df["YearMonth"] = (
    df["Year"].astype(str)
    + "-"
    + df["MonthNumber"].astype(str).str.zfill(2)
)

df["StartOfMonth"] = df["Date"].dt.to_period("M").dt.start_time

df["EndOfMonth"] = df["Date"].dt.to_period("M").dt.end_time.dt.date

# ---------------------------------
# Reordenar columnas
# ---------------------------------

df = df[
    [
        "DateKey",
        "Date",
        "Year",
        "Semester",
        "Quarter",
        "MonthNumber",
        "MonthName",
        "MonthYear",
        "YearMonth",
        "Week",
        "Day",
        "DayName",
        "DayOfYear",
        "IsWeekend",
        "StartOfMonth",
        "EndOfMonth"
    ]
]

# ---------------------------------
# Exportar
# ---------------------------------

df.to_excel(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("DimCalendar creada correctamente")
print(f"Archivo: {OUTPUT_FILE}")
print(f"Registros: {len(df):,}")
print("=" * 50)
