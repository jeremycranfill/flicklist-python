import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movieList=['Decker','The Phantom menace', 'Anime', 'Cool', 'Bad']
        randMovie = random.choice(movieList)
        return randMovie

    def get(self):
        # choose a movie by invoking our new function
        movie1 = self.getRandomMovie()
        movie2 = self.getRandomMovie()
        while movie1 == movie2:
            movie2 = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie1 + "</p>"
        content += "<h1>Movie of Tommorrow</h1>"
        content += "<p>" + movie2 + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
