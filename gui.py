import tkinter as tk
from tkinter import ttk
from config import STREAMS
from music_info_api import MusicInfoAPI  # Importiere die Musikinfo-API
import sounddevice as sd
import numpy as np
import wavio
import os


class RadioPlayerGUI:
    def __init__(self, root, radio_player, api_key):
        self.root = root
        self.radio_player = radio_player
        self.music_info_api = MusicInfoAPI(api_key)  # Instanz von MusicInfoAPI
        self.setup_ui()

    def setup_ui(self):
        # Sender Auswahl
        self.sender_label = tk.Label(self.root, text="Sender:")
        self.sender_label.grid(row=0, column=0)

        self.sender_var = tk.StringVar(value=list(STREAMS.keys())[0])  # Standardwert
        self.sender_dropdown = ttk.Combobox(self.root, textvariable=self.sender_var, values=list(STREAMS.keys()))
        self.sender_dropdown.grid(row=0, column=1)

        self.change_sender_button = tk.Button(self.root, text="Sender wechseln", command=self.change_sender)
        self.change_sender_button.grid(row=0, column=2)

        # Play, Pause und Stop Buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.radio_player.play)
        self.play_button.grid(row=1, column=0)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.radio_player.pause)
        self.pause_button.grid(row=1, column=1)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.radio_player.stop)
        self.stop_button.grid(row=1, column=2)

        # Song-Info Label
        self.song_info_label = tk.Label(self.root, text="Aktueller Song: ")
        self.song_info_label.grid(row=2, column=0, columnspan=3)

        # Knopf zur Songerkennung
        self.recognize_button = tk.Button(self.root, text="Song erkennen", command=self.recognize_song)
        self.recognize_button.grid(row=3, column=0, columnspan=3)

    def change_sender(self):
        selected_sender = self.sender_var.get()  # Den ausgewählten Sender abrufen
        stream_url = STREAMS[selected_sender]  # Die URL des ausgewählten Senders
        self.radio_player.change_stream(stream_url)  # Methode im RadioPlayer aufrufen
        self.song_info_label.config(text="Aktueller Song: ")  # Reset der Songinfo beim Senderwechsel

    def recognize_song(self):
        """Erkennt den aktuellen Song und zeigt die Informationen an."""
        audio_file_path = "temp_audio.wav"  # Temporäre Datei für die Aufnahme
        self.record_audio(10, audio_file_path)  # Nimm 10 Sekunden Audio auf

        song_info = self.music_info_api.recognize_song(audio_file_path)

        print(song_info)  # Um die Antwort der API zu überprüfen

        # Überprüfen, ob die API eine Antwort zurückgegeben hat
        if song_info is not None and 'result' in song_info:
            title = song_info['result'].get('title', 'Unbekannter Titel')
            artist = song_info['result'].get('artist', 'Unbekannter Künstler')
            self.song_info_label.config(text=f"Aktueller Song: {title} von {artist}")
        else:
            self.song_info_label.config(text="Song konnte nicht erkannt werden oder es trat ein Fehler auf.")

        # Temporäre Datei löschen
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)

    def record_audio(self, duration, filename):
        """Nimmt Audio für die angegebene Dauer auf und speichert es in einer Datei."""
        fs = 44100  # Abtastrate
        print("Aufnahme startet...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
        sd.wait()  # Warten bis die Aufnahme abgeschlossen ist
        print("Aufnahme beendet.")
        wavio.write(filename, audio, fs, sampwidth=3)  # Speichern der Audiodatei


# Beispiel für die Verwendung der GUI
if __name__ == "__main__":
    print("Starte die GUI...")
