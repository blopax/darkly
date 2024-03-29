import requests
from bs4 import BeautifulSoup
import argparse


def clean_links_list(root, root_links_list, links_list, final_list):
    final_list = final_list + [root + item for item in root_links_list if item == 'README']
    links_list = links_list + [root + item for item in root_links_list if item not in ['../', 'README']]
    return final_list, links_list


def get_links(root):
    final_list = []
    links_list = [root]
    while links_list:
        item = links_list.pop()
        r = requests.get(item)
        soup = BeautifulSoup(r.text, 'html.parser')
        tags = soup.find_all('a')
        item_links_list = [tag.get('href') for tag in tags]
        final_list += [item + element for element in item_links_list if element == 'README']
        links_list += [item + element for element in item_links_list if element not in ['../', 'README']]
    return final_list


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("root_url",
                        help="Please provide the root_url of the site provided by the iso. In this format: 10.13.0.196",
                        type=str)
        args = parser.parse_args()
        url = 'http://{}/.hidden/'.format(args.root_url)
        readme_list = get_links(url)
        answers = []
        full_answers = []
        for readme_href in readme_list:
            ret = requests.get(readme_href)
            if ret.text not in answers:
                answers.append(ret.text)
                full_answers.append({readme_href: ret.text})
        print(full_answers)
    except requests.exceptions.ConnectionError as err:
        print("There was an issue with the url provided. Check if the iso is running and provide the root_url of the "
              "site provided by the iso. In this format: 10.13.0.196")
    except:
        print("An error occured.")
