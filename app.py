# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request

# Flask constructor takes the name of
# current module (__name__) as argument.
from playlist_creator.playlist_creator import create_playlist_by_track

app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '''
	<iframe src="https://open.spotify.com/embed-legacy/playlist/24XF4Rx2JT9XRzSk5J68VX""
	width="30%" height="30%" frameborder="0" allowtransparency="true"></iframe>
	'''


@app.errorhandler(Exception)
def internal_error(error):
    return {'message': 'internal_server_error'}, 500


@app.route('/get_spotify_list', methods=['GET'])
def get_spotify_list():
    params = request.args.to_dict()
    return create_playlist_by_track(artist=params['artist'], track_name=params['track_name']), 200


# # main driver function
# if __name__ == '__main__':
#     # create_playlist_by_track(track_name='High Hopes',artist='Panic! at the disco')
#     # create_playlist_by_track(track_name='Quit', artist='Ariana Grande')
#     # run() method of Flask class runs the application
#     # on the local development server.
#     app.run()
