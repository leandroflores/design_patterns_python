from abc import ABC, abstractmethod

class Player(ABC):
    
    @abstractmethod
    def play(self, file: str) -> None:
        ...

class MP3Player(Player):

    def play(self, file: str) -> None:
        print(f"Playing MP3: {file}")

class MP4Player:

    def play_mp4(self, file_name: str) -> None:
        print(f"Playing MP4: {file_name}")


def play_audio(player, file) -> None:
    player.play(file)

mp3 = MP3Player()
play_audio(mp3, "music.mp3")

mp4 = MP4Player()
play_audio(mp4, "music.mp4")
