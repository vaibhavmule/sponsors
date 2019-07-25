import requests

from masonite import env
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class OauthController(Controller):

    def __init__(self, request: Request):
        self.request = request

    def callback(self, view: View):
        code = self.request.input('code')
        response = requests.post('https://github.com/login/oauth/access_token', json={
            'client_id': env('GITHUB_CLIENT'),
            'client_secret': env('GITHUB_SECRET'),
            'code': code}, headers={'Accept': 'application/json'})
        self.request.session.set(
            'access_token',
            response.json()['access_token'])
        return self.request.redirect('/')
