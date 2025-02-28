import pandas as pd

def read_csv(name_csv):
    # Cargar el archivo Excel (reemplaza 'archivo.xlsx' con el nombre de tu archivo)
    df = pd.read_excel(f"uploads/{name_csv}", engine="openpyxl")
    df.columns = df.columns.str.strip().str.lower()
    # Imprimir las columnas del DataFrame
    nombres = df["nombres y apellidos"].dropna().tolist()
    return nombres
