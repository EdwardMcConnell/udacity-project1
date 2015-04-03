import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://www.movieposter.com/posters/archive/main/15/A70-7642",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

usual_suspects = media.Movie("The Usual Suspects",
                             "\"The greatest trick the devil ever pulled was convincing the world he didn't exist,\" says con man Kint (Kevin Spacey), drawing a comparison to the most enigmatic criminal of all time, Keyser Soze. Kint attempts to convince the feds that the mythic crime lord not only exists, but is also responsible for drawing Kint and his four partners into a multi-million dollar heist that ended with an explosion in San Pedro Harbor - leaving few survivors.",
                             "http://www.impawards.com/1995/posters/usual_suspects_ver2.jpg",
                             "https://www.youtube.com/watch?v=oiXdPolca5w")
usual_suspects.show_trailer()