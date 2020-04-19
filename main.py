import requests
from faker import Faker
import factory

path = "https://abcdefg.xyz/auth.php"

faker = Faker()

def generate_username(*args):
    """ returns a random username """
    return faker.profile(fields=['username'])['username']

class Profile(object):
    """ Simple Profile model """
    def __init__(self, **kwargs):
        self.username = kwargs.get('username')

class ProfileFactory(factory.Factory):
    """ Generate random profile instances """
    class Meta:
        model = Profile
    username = factory.LazyAttribute(generate_username)


print('Our IP: ', requests.get('https://api.ipify.org').text)

for i in range(1, 10000000):
  print('\nRequest:', i)

  fake_username = ProfileFactory().username
  fake_words = faker.words(2)
  fake_password = fake_words[0] + fake_words[1]
  fake_data={'doAuth': 1, 'login': ProfileFactory().username, 'password':fake_password}
  print("Sending: ", fake_username, fake_password)
  r = requests.post(path, data=fake_data, allow_redirects=False)
  print(r.cookies)
  r.cookies.clear()
  print(r.status_code, r.reason)
  #print(r.text[:300] + '...')
