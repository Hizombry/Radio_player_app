import vlc
import tempfile
import shutil

class RadioPlayer:
    def __init__(self, stream_url):
        self.stream_url = stream_url
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.load_stream(self.stream_url)

    def load_stream(self, stream_url):
        """Lädt den Stream in den Player."""
        self.media = self.instance.media_new(stream_url)
        self.player.set_media(self.media)

    def play(self):
        """Spielt den Stream ab."""
        self.player.play()

    def pause(self):
        """Pauses the stream."""
        self.player.pause()

    def stop(self):
        """Stoppt den Stream."""
        self.player.stop()

    def is_playing(self):
        """Überprüft, ob der Stream spielt."""
        return self.player.is_playing()

    def set_volume(self, volume):
        """Setzt die Lautstärke des Players."""
        self.player.audio_set_volume(volume)

    def get_volume(self):
        """Gibt die aktuelle Lautstärke zurück."""
        return self.player.audio_get_volume()

    def change_stream(self, new_stream_url):
        """Wechselt den Stream."""
        self.load_stream(new_stream_url)
        self.play()

    def get_current_audio(self):
        """Gibt den aktuellen Stream als temporäre Datei zurück."""
        # Erstelle eine temporäre Datei
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        # Implementiere die Logik, um den Audio-Stream hier zu speichern.
        # Dies erfordert möglicherweise zusätzliche Bibliotheken wie pydub oder wave
        # um den Stream aufzunehmen und in die Datei zu schreiben.
        return temp_file.name  # Rückgabe des Pfads zur temporären Datei
