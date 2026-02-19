#1. Copier/coller le script et l’exécuter dans une VM.
#2. Vérifier la création du fichier report.txt.
#3. Expliquer chaque import :
#—- os, platform, socket, datetime
#4. Identifier quelles lignes peuvent échouer selon l’OS (ex : os.getlogin())
#et proposer une alternative


import os #Ce module permet d’interagir avec le système d’exploitation
import platform #Ce module donne des infos sur :Le système d’exploitation (Windows, Linux, Mac), La version, L’architecture (64 bits), Le nom de la machine
import socket #Récupérer le nom de l’ordinateur, Obtenir l’adresse IP, Créer des connexions réseau (serveur/client)
from datetime import datetime
def safe_get_hostname():
    try:
        return socket.gethostname() # ligne pouvant échouer selon l’OS 
    except Exception:
        return "UNKNOWN"
def safe_get_local_ip():
# Astuce courante pour obtenir l'IP locale sans envoyer de trafic réel
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# ligne pouvant échouer selon l’OS
        s.connect(("8.8.8.8", 80))# ligne pouvant échouer selon l’OS
        ip = s.getsockname()[0]# ligne pouvant échouer selon l’OS
        s.close()
        return ip
    except Exception:
        return "UNKNOWN"
def build_report():
    now = datetime.now().isoformat(timespec="seconds")
    report_lines = [
        f"=== SYSTEM REPORT ===",
        f"Generated: {now}",
        "",
        f"OS: {platform.system()}",
        f"OS Release: {platform.release()}",
        f"OS Version: {platform.version()}",
        f"Machine: {platform.machine()}",
        f"Architecture: {platform.architecture()}",
        f"Processor: {platform.processor()}",
        "",
        f"Hostname: {safe_get_hostname()}",
        "User: {os.getlogin() if hasattr(os, 'getlogin') else 'UNKNOWN'}",
        f"Local IP: {safe_get_local_ip()}",
    ]
    return "\n".join(report_lines)
def save_report(path="report.txt"):
    content = build_report()
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Report written to: {path}")
if __name__ == "__main__":
    save_report()