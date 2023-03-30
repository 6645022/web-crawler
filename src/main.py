import os
from lxml import html
import requests
from threading import Thread
from post import Post
from data_validation import check_post_published_time


def post_crawler(url, path):
    print(f'Starting task {url + path}...')
    response = requests.get(url + path)
    data = html.fromstring(response.content)
    tree_path = '//body/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/'
    title = data.xpath(tree_path + 'div[1]/h1/text()')[0]
    author = data.xpath(tree_path + 'div[2]/div[1]/a/text()')[0]
    date = data.xpath(tree_path + 'div[2]/div[2]/span[1]/@title')[0]
    content = requests.get(url + '/row' + path).content
    post = Post(author, title, content, date).get_post()
    print(post)
    print(f'Finish task {url + path}...')
    return


def main(url):
    try:
        print(f'Staring {url}/archive')

        response = requests.get(url + '/archive')
        tree = html.fromstring(response.content)
        tree_nodes = tree.find('body/div/div[2]/div/div/div[3]/table/tbody/tr')
        nodes = tree_nodes.xpath('//td[1]/a/@href')
        nodes_published_time = tree_nodes.xpath('//td/text()')
        print(f'page contain {len(nodes)} posts')

        threads = []
        for published_time, path in zip(nodes_published_time, nodes):
            if check_post_published_time(published_time):
                print(f'New post to scrape - {url + path}')
                t = Thread(target=post_crawler, args=(url, path,))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
        return

    except requests.exceptions.HTTPError as err:
        print(err)
        raise SystemExit(err)


if __name__ == '__main__':
    print('crawler started')
    main(os.environ.get("URL"))
