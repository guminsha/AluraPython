from movie import Movie
from serie import Serie
from playlist import Playlist
import random

avangers = Movie("Avengers - infinity war", 2020, 160)
atlanta = Serie("Atlanta", 2018, 2)
scary_movie = Movie("Scary movie", 1999, 100)
daredevil = Serie("Daredevil", 2016, 2)
resident_evil = Movie("Resident evil 4", 2014, 130)

movies_series = [avangers, atlanta, daredevil, scary_movie]

for i in range(0,100):
	rad_choice = random.choice(movies_series)
	rad_choice.new_like()

weekend_playlist = Playlist("Weekend Playlist", movies_series)

for program in weekend_playlist:
	print(program)

print(f"Playlist size is: {len(weekend_playlist)}")
print(f"{daredevil.name} is in Playlist? {weekend_playlist.verify(daredevil)}")

# for program in movies_series:
# 	detail = program.duration if hasattr(program, "duration") else program.seasons
# 	print(f"{program.name} - {detail} - {program.likes}")