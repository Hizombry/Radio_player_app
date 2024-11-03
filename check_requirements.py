import importlib
import subprocess
import sys

# Liste der benötigten Pakete (aktualisiert)
required_packages = [
    "spotipy", "requests", "pydub", "scipy", "numpy", "librosa"
]

missing_packages = []

for package in required_packages:
    try:
        importlib.import_module(package)
    except ImportError:
        missing_packages.append(package)

# Überprüfung, ob tkinter installiert ist
try:
    import tkinter
except ImportError:
    missing_packages.append("tkinter")

try:
    import vlc
except ImportError:
    missing_packages.append("python-vlc")

if missing_packages:
    print("Die folgenden Pakete sind nicht installiert:")
    for package in missing_packages:
        print(f"- {package}")

    print("\nInstalliere fehlende Pakete mit:")
    print("pip install " + " ".join(missing_packages))

    # Optional: Automatische Installation der fehlenden Pakete
    user_input = input("\nMöchtest du die fehlenden Pakete automatisch installieren? (y/n): ")
    if user_input.lower() == 'y':
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Installieren der Pakete: {e}")
else:
    print("Alle benötigten Pakete sind installiert.")
