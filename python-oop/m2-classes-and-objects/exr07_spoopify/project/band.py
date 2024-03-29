import sys, os
sys.path.insert(0, os.getcwd())
from exr07_spoopify.project.song import Song
from exr07_spoopify.project.album import Album


class Band:
    def __init__(self, name: str) -> None:
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name):
        album = [a for a in self.albums if a.name == album_name]
        if album:
            album = album[0]
            if album.published:
                return f'Album has been published. It cannot be removed.'
            else:
                self.albums.remove(album)
                return f'Album {album.name} has been removed.'

        return f'Album {album_name} is not found.'

    def details(self):
        message = f'Band {self.name}\n'
        for album in self.albums:
            message += album.details()

        return message


if __name__ == '__main__':
    song = Song('Running in the 90s', 3.45, False)
    print(song.get_info())

    album = Album('Initial D', song)
    second_song = Song('Around the World', 2.34, False)
    print(album.add_song(second_song))
    print(album.details())
    print(album.publish())

    band = Band('Manuel')
    print(band.add_album(album))
    print(band.remove_album('Initial D'))
    print(band.details())
