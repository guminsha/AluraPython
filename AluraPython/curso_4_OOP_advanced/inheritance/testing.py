from movie import Movie
from serie import Serie

avangers = Movie("Avengers - infinity war", 2020, 160)
atlanta = Serie("Atlanta", 2018, 2)

avangers.new_like()
avangers.new_like()
atlanta.new_like()

avangers.show_info()
atlanta.show_info()