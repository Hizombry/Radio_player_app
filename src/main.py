import tkinter as tk  # Stellt sicher, dass tkinter importiert wird
from player import RadioPlayer
from gui import RadioPlayerGUI
from config import STREAMS, my_secret  # Hier importieren wir die STREAMS und den API-Schlüssel

def main():
    print("Initialisiere GUI und Komponenten")  # Debug-Ausgabe

    # Tkinter Root-Setup
    root = tk.Tk()
    root.title("Radio Player")

    # Lade den Standard-Stream (Erster Stream in der Liste)
    default_stream_url = list(STREAMS.values())[0]  # Erster Stream in der Liste
    radio_player = RadioPlayer(default_stream_url)

    # Erstelle GUI und verbinde die Module
    app = RadioPlayerGUI(root, radio_player, my_secret)

    # Starte die GUI
    root.mainloop()

if __name__ == "__main__":
    main()
