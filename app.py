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

# Path to the directory containing JSON files
json_dir = r"C:\Users\Antonio\Desktop\Freelancing\Oikos\dashboard\data\CMV"

# Recursively walk through the directory and process each JSON file
for root, dirs, files in os.walk(json_dir):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    # print(f"Loaded {file}:", data["riskFactors"])
                    riskFactors = data["riskFactors"]
                    print(file)
                    print("total:", total_score(riskFactors))
                    print("avg:", average_risk(riskFactors))
                    print("urgency_1_100:", urgency_1_to_100(riskFactors))
                    
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")