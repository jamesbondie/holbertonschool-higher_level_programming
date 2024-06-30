import requests
import csv





def fetch_and_print_posts():
    requ = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(requ.status_code))
    for i in requ.json():
        print(i['title'])

def fetch_and_save_posts():
    requ = requests.get('https://jsonplaceholder.typicode.com/posts')
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
