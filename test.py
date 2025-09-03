import json
from app import urgency_1_to_100
import os
import pprint

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
def transform_employee_json(data: dict, idx_data: dict) -> dict:
    """
    Trasforma un record JSON dettagliato di un dipendente in un formato di riepilogo.

    Args:
        data: Il dizionario JSON di input.
        idx_data: Il dizionario JSON di indice.

    Returns:
        Il dizionario JSON trasformato.
    """
    # --- Mappature dirette e derivate ---
    name = data.get("name", "")
    area = data.get("department", "").replace("Area ", "")
    file_name = name.replace(" ", "")
    
    for item in idx_data:
        if item.get("name") == name:
            idx_data = item
            break

    return {
        "id": data.get("id"),
        "file_path": f"data/{area}/{file_name}.json",
        "name": name,
        "role": data.get("role"),
        "area": area,
        "sub_area": idx_data.get("sub_area"),
        "keywords": idx_data.get("description", []),
        "urgency": urgency_1_to_100(data.get("riskFactors", {})),
    }

json_dir = r"C:\Users\Antonio\Desktop\Freelancing\Oikos\dashboard\data\GOA"
index_data = load_json_file(r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index_goa.json")
new_data = []
for root, dirs, files in os.walk(json_dir):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            file_data = load_json_file(file_path)
            print(file_path)
            tmp_data = transform_employee_json(file_data, index_data)
            new_data.append(tmp_data)

with open(r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index_goa_tot.json", 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

            