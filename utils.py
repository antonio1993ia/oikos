import os
import json

def load_json_file(file_path: str) -> dict:
    """
    Carica un file JSON e restituisce il suo contenuto come dizionario.

    Args:
        file_path: Il percorso del file JSON da caricare.

    Returns:
        Il contenuto del file JSON come dizionario.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def metti_insieme_files_index(json_dir: str) -> list:
    """
    Combina i file JSON dei dipendenti con i dati dell'indice in un nuovo formato.

    Args:
        json_dir: La directory contenente i file JSON dei dipendenti.
        index_data: La lista di dizionari dell'indice dati.

    Returns:
        Una lista di dizionari JSON trasformati.
    """
    new_data = []
    for root, dirs, files in os.walk(json_dir):
        for file in files:
            if file in ["index_oa.json", "index_cmv.json", "index_goa.json"]:
                print(file)
                tmp_list = load_json_file(os.path.join(root, file))
                print(len(tmp_list))
                new_data.extend(tmp_list)
    print(f"Total records combined: {len(new_data)}") 
    return new_data

                
def remove_key_from_dict(data: dict, key: str) -> dict:
    """
    Rimuove una chiave specifica da un dizionario se esiste.

    Args:
        data: Il dizionario da cui rimuovere la chiave.
        key: La chiave da rimuovere.

    Returns:
        Il dizionario aggiornato senza la chiave specificata.
    """
    if key in data:
        del data[key]
    return data


# json_dir = r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data"
# new = metti_insieme_files_index()

# # data = load_json_file(r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index_new.json")
# # for item in data:
# #     remove_key_from_dict(item, "file_path")
# with open(r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index_new_0.json", 'w', encoding='utf-8') as index_file:
#     json.dump(new, index_file, indent=4, ensure_ascii=False)

filepath = r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index_new_0.json"
index_data = load_json_file(filepath)
print(len(index_data))
    
