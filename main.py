# BeeLaw

from flask import Flask, request
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

terrible_movies = ['Nine Lives', 'Love Actually']

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
        {0}
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label>
            I want to add
            <input type="text" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# a form for crossing off watched movies
crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                <option value="Star Wars">Star Wars</option>
                <option value="My Favorite Martian">My Favorite Martian</option>
                <option value="The Avengers">The Avengers</option>
                <option value="The Hitchhiker's Guide To The Galaxy">The Hitchhiker's Guide To The Galaxy</option>
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
"""


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']
    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
    content = page_header.format('') + "<p>" + confirmation + "</p>" + add_form + crossoff_form + page_footer

    return content


@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # build response content
    if not new_movie:
        return page_header.format('Please specify the name of the movie you want to add') + add_form + crossoff_form + page_footer
    new_movie_element = "<strong>" + cgi.escape(new_movie) + "</strong>"
    if new_movie in terrible_movies:
        return page_header.format("Trust me, you don't want to add " + new_movie + " to the list") + add_form + crossoff_form + page_footer
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header.format('') + "<p>" + sentence + "</p>" + add_form + crossoff_form + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # build the response string
    content = page_header.format('') + edit_header + add_form + crossoff_form + page_footer

    return content


app.run()

