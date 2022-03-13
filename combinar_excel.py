import pandas as pd
files = ['Ruta Nombre_fichero_1', 'Ruta Nombre_fichero_2', 'Ruta Nombre_fichero_3', 'Ruta Nombre_fichero_4']
excel_unificado = pd.DataFrame()

for file in files:
  df = pd.read_excel(file, skiprows = 1)
  excel_unificado = excel_unificado(df, ignore_index = True)
  
excel_unificado.to_excel('excel_unificado.xlsx')
