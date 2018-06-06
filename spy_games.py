import requests


class UserVk:
    user_id = None
    access_token = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
    version_api = '5.8'

    def __init__(self, name):
        response = requests.get('https://api.vk.com/method/users.get', {
            'user_ids': name,
            'access_token': self.access_token,
            'v': self.version_api
        })
        try:
            self.user_id = response.json()['response'][0]['id']
        except KeyError:
            self.user_id = None

    def get_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get', {
            'user_id': self.user_id,
            'access_token': self.access_token,
            'v': self.version_api
        })
        return response.json()['response']['items']

    def get_groups(self):
        response = requests.get('https://api.vk.com/method/groups.get', {
            'user_id': self.user_id,
            'access_token': self.access_token,
            'v': self.version_api
        })
        return response.json()['response']['items']


name = 424364020
a = UserVk(name)
b = a.get_friends()
c = a.get_groups()
print(b)
print(c)



