class PhotoAlbum:
    def __init__(self, pages) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)
    
    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f'{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}'
        
        return f'No more free slots'

    def display(self):
        display = f'{"-" * 11}\n'
        for page in self.photos:
            photos_per_curr_page = len(page)
            if photos_per_curr_page > 0:
                display += f'{"[] " * (photos_per_curr_page - 1)}[]\n'
                display += f'{"-" * 11}\n'
        
        return display


if __name__ == '__main__':
    album = PhotoAlbum(3)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))

    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())
