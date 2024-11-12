# test_player.py
from player import RadioPlayer


def test_radio_player():
    stream_url = "https://example-stream-url.com/radio"
    player = RadioPlayer(stream_url)

    player.play()
    assert player.is_playing_status() == True, "Der Player sollte spielen."

    player.pause()
    assert player.is_playing_status() == False, "Der Player sollte pausiert sein."

    player.stop()
    assert player.is_playing_status() == False, "Der Player sollte gestoppt sein."


test_radio_player()
