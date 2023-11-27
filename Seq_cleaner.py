import os
import pandas as pd

def process_phd_file(file_path, header_lines=5):
    nucleotides = []
    qualities = []

    with open(file_path, "r") as file:
        for i in range(header_lines):
            next(file)  # skip the current line

        in_final_section = False

        for line in file:
            line = line.strip()
            if line.startswith("END") or not line:
                in_final_section = True
            if not in_final_section:
                parts = line.split() 
                if len(parts) >= 2:
                    nucleotides.append(parts[0])
                    qualities.append(int(parts[1]))  

    data = {'Nucleótides': nucleotides, 'Qualities': qualities}
    df = pd.DataFrame(data)
    return df

def procesar_folder(folder_path):
    # Create the "curated_sequence" folder if it doesn´t exist
    curated_folder = os.path.join(folder_path, "curated_sequences")
    os.makedirs(curated_folder, exist_ok=True)

    for file in os.listdir(carpeta_path):
        archivo_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and archivo.lower().endswith(".phd"): 
            df_temp = process_phd_files(file_path, header_lines=5)

            # Perform additional operations as needed with the DataFrame df_temp
            # ...

            # print df_temp if needed
            print(df_temp)

            # filter and save the DataFrame to a new file
            filter_value = 30
            new_df = df_temp[df_temp['Qualities'] >= filter_value]

            # Create FASTA file
            nucleotide_list = new_df['Nucleótides'].tolist()

            # File name without extension
            name_without_extension = os.path.splitext(file)[0]

            # Crear el nombre del archivo FASTA con el nombre del archivo original
            fasta_file_name = f'nucleotides_{name_without_extension}.fasta'
            fasta_file_path = os.path.join(curated_folder, fasta_file_name)

            # Save the FASTA file with the original file name as the identifier
            with open(fasta_file_path, 'w') as fasta_file:
                fasta_file.write(f">{name_without_extension}\n{''.join(nucleotide_list)}\n")

# Call the funtion and pass the folder containing the files
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python archive.py folder address")
        sys.exit(1)

    folder_with_files = sys.argv[1]
    process_folder(folder_with_files)










