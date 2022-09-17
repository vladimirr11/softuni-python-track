import sys, os
sys.path.insert(0, os.getcwd())
from exr07_spoopify.project.song import Song


class Album:
    def __init__(self, name: str, songs=None) -> None:
        self.name = name

        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs

        self.published = False

    def add_song(self, song: Song):
        s = [s for s in self.songs if s.name == song.name]
        if s:
            s = s[0]
            if s.single:
                return f'Cannot add {s.name}. It\'s a single.'
            else:
                return f'Song is already in the album.'

        if self.published:
            return f'Cannot add songs. Album is published.'

        self.songs.append(song)
        song = self.songs[-1]
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        song = [s for s in self.songs if s.name == song_name]
        if song and not self.published:
            self.songs.remove(song[0])
            return f'Removed song {song_name} from album {self.name}.'

        if self.published:
            return f'Cannot remove songs. Album is published.'

        if len(song) == 0:
            return f'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'{self.name} is already published.'

        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        message = f'Album {self.name}\n'
        for song in self.songs:
            message += f'== {song.get_info()}\n'

        return message
