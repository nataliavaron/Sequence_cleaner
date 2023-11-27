import os
import pandas as pd

def procesar_archivo_phd(file_path, header_lines=5):
    nucleotidos = []
    calidades = []

    with open(file_path, "r") as file:
        for i in range(header_lines):
            next(file)  # Salta la línea actual

        in_final_section = False

        for line in file:
            line = line.strip()
            if line.startswith("END") or not line:
                in_final_section = True
            if not in_final_section:
                parts = line.split()  # Suponiendo que las secuencias y calidades están separadas por espacios
                if len(parts) >= 2:
                    nucleotidos.append(parts[0])
                    calidades.append(int(parts[1]))  # Convierte la calidad a un número entero

    data = {'Nucleótidos': nucleotidos, 'Calidades': calidades}
    df = pd.DataFrame(data)
    return df

def procesar_carpeta(carpeta_path):
    # Crear la carpeta "secuencias_curadas" si no existe
    carpeta_curada = os.path.join(carpeta_path, "secuencias_curadas")
    os.makedirs(carpeta_curada, exist_ok=True)

    for archivo in os.listdir(carpeta_path):
        archivo_path = os.path.join(carpeta_path, archivo)
        if os.path.isfile(archivo_path) and archivo.lower().endswith(".phd"):  # Filtrar por archivos .phd
            df_temp = procesar_archivo_phd(archivo_path, header_lines=5)

            # Realizar operaciones adicionales según sea necesario con el DataFrame df_temp
            # ...

            # Puedes imprimir o hacer cualquier cosa con df_temp si lo necesitas
            print(df_temp)

            # Filtrar y guardar el DataFrame en un nuevo archivo
            valor_filtro = 30
            nuevo_df = df_temp[df_temp['Calidades'] >= valor_filtro]

            # Crear archivo FASTA
            lista_nucleotidos = nuevo_df['Nucleótidos'].tolist()

            # Nombre del archivo sin la extensión
            nombre_sin_extension = os.path.splitext(archivo)[0]

            # Crear el nombre del archivo FASTA con el nombre del archivo original
            fasta_file_name = f'nucleotidos_{nombre_sin_extension}.fasta'
            fasta_file_path = os.path.join(carpeta_curada, fasta_file_name)

            # Guardar el archivo FASTA con el nombre del archivo original como identificador
            with open(fasta_file_path, 'w') as fasta_file:
                fasta_file.write(f">{nombre_sin_extension}\n{''.join(lista_nucleotidos)}\n")

# Llamar a la función y pasar la carpeta que contiene los archivos
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python ensayo.py C:/Users/Diego Toro/Desktop/Archivos_clase/Proyecto final/Secuencias_sanger")
        sys.exit(1)

    carpeta_con_archivos = sys.argv[1]
    procesar_carpeta(carpeta_con_archivos)










