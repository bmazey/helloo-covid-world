import requests


def call_api():
    response = requests.get('https://covid-19-testing.github.io/locations/new-york/complete.json')
    print(str(response.json()))


if __name__ == '__main__':
    call_api()
