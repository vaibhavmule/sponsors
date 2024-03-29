from masonite import env
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from github import Github


class PageController(Controller):

    def __init__(self, request: Request):
        self.request = request

    def index(self, view: View):
        client_id = env('GITHUB_CLIENT')
        access_token = self.request.session.get('access_token')
        response = {'client_id': client_id, 'repos': []}
        
        if access_token:
            g = Github(access_token)
            print(g.get_user().name)
            response['repos'] = g.get_user().get_repos()
            repo = g.get_repo('vaibhavmule/vetted-interview')
            contents = repo.get_contents("README.md")
            print(contents, repo)
            file = repo.create_file('.github/FUNDING.yml', 'Create FUNDING.yml', '# These are supported funding model platforms \n\n custom: paypal.me/VaibhavMule \n\n # Generated by @vaibhavmule')
            print(file)

        return view.render('index', response)
