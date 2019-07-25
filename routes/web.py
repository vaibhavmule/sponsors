"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'PageController@index').name('home'),
    # Github
    Get().route('/auth/github', 'OauthController@auth'),
    Get().route('/auth/github/callback', 'OauthController@callback'),
]
