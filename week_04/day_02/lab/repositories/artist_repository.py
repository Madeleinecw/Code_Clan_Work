from db.run_sql import run_sql
from models.artist import Artist



def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name] 
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        artist = Artist(results['name'], results['id'])
    return artist

def get_artist(album):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [album.id]
    results = run_sql(sql, values)[0]
    if results is not None:
        artist = Artist(results['name'], results['id'])
    return artist