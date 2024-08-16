import pandas as pd
import numpy as np

df = pd.read_csv('results.csv')

for r in range(len(df)):
    raio = df.iloc[r,6]
    comprimento = df.iloc[r,4]
    resistencia = (df.iloc[r,8] + df.iloc[r,9])/2
    area = np.pi * (raio ** 2)
    resistividade = (area * resistencia)/comprimento
    
    # print(f"Área: {area:.5f}")
    print(f"Resistividade: {resistividade:.2f}")