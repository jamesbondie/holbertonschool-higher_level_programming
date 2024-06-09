import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'
requ = requests.get(url)


def fetch_and_print_posts():
    print("Status code:", requ.status_code)
    for i in requ.json():
        print(i['title'])

def fetch_and_save_posts():
    print(requ.status_code)
    with open('posts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for date in requ.json():
            writer.writerow({'id': date['id'],
                            'title': date['title'],
                            'body': date['id']})

fetch_and_print_posts()
fetch_and_save_posts()
