from github import Github

from config import PLATFORMS, FIlE_PATH


def sponsor(funding_site):
    message = ('# These are supported funding model platforms\n\n')
    for funding in funding_site:
        if funding in PLATFORMS:
            message += f'{funding}: {funding_site[funding]}\n'
    message += '\n# generated by vaibhavmule/sponsor, sponsor me at patreon: vaibhavmule\n'
    return message


def generate_file(content):
    pass

def repos(username):
    g = Github("vaibhavmule", "raj-13579")
    api_url = f'https://api.github.com/users/{username}/repositories'
    return g.get_user().get_repos(visibility='public')


if __name__ == "__main__":
    funding_site = {
        'github': ['vaibhavmule', 'josephmancuso'],
        'patreon': 'vaibhavmule',
        'custom': 'https://www.paypal.me/VaibhavMule',
        'paypal': 'https://www.paypal.me/VaibhavMule',
    }
    print(sponsor(funding_site))
    for repo in repos('vaibhavmule'):
        if not repo.fork:
            print(repo.name)