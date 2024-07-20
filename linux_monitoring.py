#Module subprocess pour vérifier si le module psutil est a installer
import subprocess

#Tente d'importer psutil et l'install si pas possible
try:
    import psutil
except ImportError:
    subprocess.check_call([
        "python", "-m", "pip", "install", "psutil"
        ])

#Reiponrte psutil si il était en erreur
import psutil


# Utilisation du CPU
cpu_percent = psutil.cpu_percent(interval=1)
print(f"Utilisation CPU : {cpu_percent}%")

# Utilisation de la RAM
ram = psutil.virtual_memory()
ram_total = ram.total / (1024 * 1024 * 1024)  # Conversion en Go
ram_used = ram.used / (1024 * 1024 * 1024)    # Conversion en Go
ram_percent = ram.percent
print(f"RAM totale : {ram_total:.2f} Go")
print(f"RAM utilisée : {ram_used:.2f} Go")
print(f"Pourcentage RAM utilisée : {ram_percent}%")

# Utilisation du stockage
disk = psutil.disk_usage('/')
disk_total = disk.total / (1024 * 1024 * 1024)  # Conversion en Go
disk_used = disk.used / (1024 * 1024 * 1024)    # Conversion en Go
disk_percent = disk.percent
print(f"Stockage total : {disk_total:.2f} Go")
print(f"Stockage utilisé : {disk_used:.2f} Go")
print(f"Pourcentage stockage utilisé : {disk_percent}%")
