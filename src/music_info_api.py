import requests
from config import my_secret  # Stelle sicher, dass dieser Schlüssel in config.py definiert ist

class MusicInfoAPI:
    def __init__(self, api_key):
        self.audd_api_key = api_key

    def recognize_song(self, audio_file_path):
        """Erkennt den aktuellen Song mit AudD."""
        url = "https://api.audd.io/"
        with open(audio_file_path, 'rb') as audio_file:
            files = {
                'file': audio_file,
            }
            data = {
                'api_token': self.audd_api_key,
            }
            response = requests.post(url, files=files, data=data)
            if response.status_code == 200:
                return response.json()  # Rückgabe der JSON-Daten
            else:
                print(f"Fehler beim Abrufen von AudD-Daten: {response.status_code}")
                return None

# Beispiel für die Verwendung der API
if __name__ == "__main__":
    api = MusicInfoAPI(my_secret)
    song_info = api.recognize_song("path_to_your_audio_file.wav")  # Ersetze dies mit einer gültigen Datei
    if song_info:
        print(song_info)
