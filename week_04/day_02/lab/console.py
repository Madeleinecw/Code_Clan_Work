import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist('Kate Bush')
album_1 = Album('Hounds of Love', 'Pop', artist_1)

artist_repository.save(artist_1)
album_repository.save(album_1)
artist_repository.select_all()
album_repository.select_all()

pdb.set_trace()