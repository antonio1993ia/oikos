import os
import json
from typing import Dict, Any

METRICS = [
    "importanza_processo","copertura_documentazione","livello_formalizzazione",
    "indice_insostituibilita","tasso_cambiamento","impatto_downstream",
    "maturita_strumenti","facilita_passaggio_consegne","impatto_cliente",
    "sensibilita_dati","punti_singoli_fallimento","segnale_rilavorazione",
    "tracciabilita_errori","livello_automazione","tempo_ripristino",
    "qualita_controlli","frammentazione_integrazioni",
]

def normalize_factors(factors: Dict[str, Any]) -> Dict[str, float]:
    n = {}
    for k in METRICS:
        v = factors.get(k, 0) or 0
        if k == "importanza_processo":
            n[k] = max(0.0, min(1.0, (float(v) - 1.0) / 4.0))
        else:
            n[k] = float(v)
    return n

def total_score(factors: Dict[str, Any]) -> float:
    n = normalize_factors(factors)
    return sum(n.values())

def average_risk(factors: Dict[str, Any]) -> float:
    return total_score(factors) / len(METRICS)

def urgency_1_to_100(factors: Dict[str, Any]) -> int:
    # stesso mapping usato nel frontend: 1..100
    avg = average_risk(factors)
    return round(avg * 99 + 1)

def transform_employee_json(data: dict) -> dict:
    """
    Trasforma un record JSON dettagliato di un dipendente in un formato di riepilogo.

    Args:
        data: Il dizionario JSON di input.

    Returns:
        Il dizionario JSON trasformato.
    """
    # --- Mappature dirette e derivate ---
    name = data.get("name", "")
    area = data.get("department", "").replace("Area ", "")
    file_name = name.replace(" ", "")

    return {
        "id": data.get("id"),
        "file_path": f"data/{area}/{file_name}.json",
        "name": name,
        "role": data.get("role"),
        "area": area,
        "sub_area": data.get("section"),
        "urgency": urgency_1_to_100(data.get("riskFactors", {})),
    }



# Path to the directory containing JSON files
# json_dir = r"C:\Users\Antonio\Desktop\Freelancing\Oikos\dashboard\data\GOA"
# new = []

# indexpath = r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index.json"
# with open(indexpath, "r") as f:
#     index_data = json.load(f)  # data is a list of dicts

# # Recursively walk through the directory and process each JSON file

# for root, dirs, files in os.walk(json_dir):
#     for file in files:
#         if file.endswith('.json'):
#             file_path = os.path.join(root, file)
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 try:
#                     tmp_data = json.load(f)
#                     riskFactors = tmp_data["riskFactors"]
                    
#                     nome = tmp_data.get("name", "N/A")
                    
#                     update_json_index(nome, urgency_1_to_100(riskFactors), index_data)
#                     for item in index_data:
#                         if item.get("name") == nome:
#                             item["urgency"] = urgency_1_to_100(riskFactors)
#                             new.append(item)
#                             print(f"{len(new)}")
#                             break
#                 except Exception as e:
#                     print(f"Error loading {file_path}: {e}")
# with open(r"C:\Users\Antonio\Desktop\Freelancing\Oikos\oikos_github\data\index_new.json", 'w', encoding='utf-8') as index_file:
#     json.dump(new, index_file, indent=4)
    
# # save back to file
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)
