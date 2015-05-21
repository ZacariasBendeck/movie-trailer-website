import media
import fresh_tomatoes


#This is the the data of my movies using classes
interstellar = media.Movie('Interstellar','A former astronaut tries to save humanity from extinction',
                           'http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
                           'https://www.youtube.com/watch?v=3WzHXI5HizQ')

groundhog_day = media.Movie("Groundhog Day", 'A newsanchor gets stuck reliving the same day over and over again.',
                             'http://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg',
                            'https://www.youtube.com/watch?v=tSVeDx9fk60')
prometheus = media.Movie('Prometheus', 'Scientist travel through space in search of aliens based on cave painting',
                         'http://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg',
                         'https://www.youtube.com/watch?v=sftuxbvGwiU')
pulp_fiction = media.Movie('Pulp Fiction','',
                           'http://upload.wikimedia.org/wikipedia/en/thumb/8/82/Pulp_Fiction_cover.jpg/220px-Pulp_Fiction_cover.jpg',
                           'https://www.youtube.com/watch?v=s7EdQ4FqbhY')

dragnet = media.Movie('Dragnet','','http://upload.wikimedia.org/wikipedia/en/8/8a/Dragnet_movie.jpg',
                      'https://www.youtube.com/watch?v=JZL7epLIyhA')

spaceballs = media.Movie('Spaceballs', '','http://upload.wikimedia.org/wikipedia/en/4/45/Spaceballs.jpg',
                         'https://www.youtube.com/watch?v=0uzEgsHypgM')

#assigning all the movies to a variable to send to the fresh tomatoes function
movies = [interstellar,groundhog_day,prometheus,pulp_fiction,dragnet,spaceballs]

#call function from fresh_tomatoes.py to make the html page and open the page movies in the webbrowser
fresh_tomatoes.open_movies_page(movies)

