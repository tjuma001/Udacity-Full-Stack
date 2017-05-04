import media
import fresh_tomatoes


def main():

    # Toy Story movie instance
    toy_story = media.Movie(
        "Toy Story",
        "A story of a body and his toys that come to life",
        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    # Avatar movie instance
    avatar = media.Movie(
        "Avatar",
        "A marine on an alien planet",
        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

    # Harry Potter movie instance
    harry_potter = media.Movie(
        "Harry Potter and the Philosophers Stone",
        "A wizard with his two friends going on wizard adventures.",
        "http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster.jpg",
        "https://www.youtube.com/watch?v=eKSB0gXl9dw")

    # Hunger Games movie instance
    hunger_games = media.Movie(
        "Hunger Games",
        "Survival of the fitess",
        "https://vignette1.wikia.nocookie.net/thehungergames/images/c/cd/Dvd20.jpeg/revision/latest?cb=20120806204941",
        "https://www.youtube.com/watch?v=mfmrPu43DF8")

    # Guardians of the Galaxy movie instance
    guardian_galaxy = media.Movie(
        "Guardians of the Galaxy",
        "A classic superhero movie",
        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
        "https://www.youtube.com/watch?v=d96cjJhvlMA")

    # Star Wars movie instance
    star_wars = media.Movie(
        "Star Wars",
        "A long time ago in a galaxy far far away...",
        "http://theenchantedmanor.com/wp-content/uploads/2016/05/Star-Wars-poster-of-original-film.jpg",
        "https://www.youtube.com/watch?v=vP_1T4ilm8M")

    # Movie array
    movies = [toy_story, avatar, harry_potter, hunger_games, guardian_galaxy, star_wars]

    # Using the fresh_tomatoes module, create the movie's web page
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
