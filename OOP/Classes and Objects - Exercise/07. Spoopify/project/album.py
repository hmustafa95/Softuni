from song import Song

class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name not in [song.name for song in self.songs]:
            return "Song is not in the album."
        remove_song = next(filter(lambda s: s.name == song_name, self.songs))
        self.songs.remove(remove_song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f'Album {self.name}']
        for song in self.songs:
            info.append(f'== {song.get_info()}')
        return '\n'.join(info)

