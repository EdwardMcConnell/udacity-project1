import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "https://www.movieposter.com/posters/archive/main/15/A70-7642",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

usual_suspects = media.Movie("The Usual Suspects",
                             "http://www.impawards.com/1995/posters/usual_suspects_ver2.jpg",
                             "https://www.youtube.com/watch?v=oiXdPolca5w")

school_of_rock = media.Movie("School of Rock",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


movies = [toy_story, avatar, usual_suspects, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
