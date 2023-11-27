# Sequence_cleaner
This Python script is tailored for handling .phd files from Sanger sequencing. It extracts nucleotide sequences, omitting regions with low quality. Designed for command line execution, its automatically produces refined FASTA files in a designated folder. It proves particularly beneficial for bioinformatics
# what does this?
This Python script manages the processing of files with the .phd extension, originating from Sanger sequencing data. It is a crucial tool for cleaning these files, as they contain intricate details about the quality of each nucleotide. This information facilitates the exclusion of regions with low sequence quality. Specifically, nucleotides with a Phred quality score lower than 30 are omitted.
# Why the project is useful?
This project is of paramount importance as it provides a user-friendly tool for the analysis of Sanger sequencing data. The absence of such automated processes significantly hinders crucial bioinformatic analysis in molecular biology and genetics research. By offering an automated solution, our project streamlines the sequencing data processing task, allowing researchers to focus on more substantive aspects of their investigations and accelerating progress in understanding molecular biology and genetics.
# Goal
Designed to be executed from the command line, the code automates the processing and filtering of nucleotide sequences from .phd files. As a result, it generates optimized FASTA files stored in a designated folder. This approach is particularly valuable in bioinformatics projects involving the analysis of Sanger sequencing data.

# Python script 
# 1. Processing files with the .phd extension: In this first part, the function receives the path of a file with the .phd extension and an optional number of header lines (header_lines). It reads the file, skips the specified header lines, and processes the remaining information. It extracts nucleotide sequences and their corresponding qualities, creating a pandas DataFrame with two columns: 'Nucleotides' and 'Qualities. 
mport os
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
    
# 2. Folder path for processing and quality filtering of sequences: This function receives the path of a folder containing .phd files. It creates a subfolder named 'curated_sequences' within the original folder (or locates it if it already exists). 
ef procesar_folder(folder_path):
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
    
# 3. Filtering of sequences: It iterates over each .phd file in the source folder, calling the 'process_phd_file' function to obtain a DataFrame with sequences and qualities. This allows the filtering of sequences based on a quality threshold (30 in this case), and it saves the filtered sequences as FASTA files in the 'curated_sequences' folder. 

  # filter and save the DataFrame to a new file
            filter_value = 30
            new_df = df_temp[df_temp['Qualities'] >= filter_value]
  # Create FASTA file
            nucleotide_list = new_df['Nucleótides'].tolist()

            # File name without extension
            name_without_extension = os.path.splitext(file)[0]

            # Create the FASTA file name using the original file name.
            fasta_file_name = f'nucleotides_{name_without_extension}.fasta'
            fasta_file_path = os.path.join(curated_folder, fasta_file_name)

            # Save the FASTA file with the original file name as the identifier
            with open(fasta_file_path, 'w') as fasta_file:
                fasta_file.write(f">{name_without_extension}\n{''.join(nucleotide_list)}\n")
                
  # 4. Main Block:  Script verification: checks if it is being executed directly. If so, it awaits the user to provide the path to the folder containing the .phd files as a command line argument. If the path is not provided, it displays a usage message. Finally, it calls the process_folder function with the provided folder as an argument.
  
      # Call the funtion and pass the folder containing the files
if _name_ == "_main_":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python archive.py folder address")
        sys.exit(1)

    folder_with_files = sys.argv[1]
    process_folder(folder_with_files)
