import requests
from bs4 import BeautifulSoup


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
        readme_list = get_links('http://10.13.0.196/.hidden/')
        answers = []
        full_answers = []
        for readme_href in readme_list:
            ret = requests.get(readme_href)
            if ret.text not in answers:
                answers.append(ret.text)
                full_answers.append({readme_href: ret.text})
        print(full_answers)
    except requests.exceptions.ConnectionError as err:
        print("There was an issue. Modify the line 27 of the file to be sure it is the correct url of the website.")
    except:
        print("An error occured.")
