# 01_EDA.py – Exploratory Data Analysis for matbench dataset

import pandas as pd
import matplotlib.pyplot as plt
from matminer.datasets import load_dataset

# Cargar el dataset
df = load_dataset("matbench_mp_e_form")

print("Número de muestras:", len(df))
print("Columnas:", df.columns.tolist())
print("\nPrimeras filas:")
print(df.head())

print("\nEstadísticas:")
print(df.describe())

# Histograma de energía de formación
plt.hist(df["e_form"], bins=50, color="skyblue", edgecolor="black")
plt.title("Distribución de energía de formación (e_form)")
plt.xlabel("e_form (eV/atom)")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()
