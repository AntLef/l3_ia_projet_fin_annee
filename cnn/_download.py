import os
import requests
import threading
from bs4 import BeautifulSoup

import requests
import os
from PIL import Image
import io
import hashlib

from _params import *


print()


def executeThread_r(i, j, id_r):

    def download_images(data, Image_Folder, id_r):
        imagelinks = []
        num_images = 500
        count = 1

        print('Searching Images ' + data + '....')

        while len(imagelinks) < num_images and count < 45:
            count = count + 1
            print(count)
            
            search_url = "https://www.istockphoto.com/fr/search/2/image?mediatype=photography&page=" + str(
                count) + "&phrase=" + ("chien" if id_r < 5 else "chat") + "%2520" + str(data).replace(" ", "%2520")
            
            response = requests.get(search_url)
            html = response.text

            b_soup = BeautifulSoup(html, 'html.parser')
            results = b_soup.findAll('figure', {'class': 'MosiacAsset-module__figure___1gQVb'})

            for res in results:
                if res.find('img').get('src') is None:
                    imagelinks.append(res.find('img').get('data-src'))
                else:
                    imagelinks.append(res.find('img').get('src'))

        # print(f'Found {len(imagelinks)} images')
        print('Start downloading...')

        for i, imagelink in enumerate(imagelinks):

            response = requests.get(imagelink).content

            image_file = io.BytesIO(response)
            image = Image.open(image_file).convert('RGB')

            imagename = ("0" if id_r < 5 else "1") + "_" + str(id_r) + "_0_" + str(i + 1) + '.jpg'

            with open(hashlib.sha1(response).hexdigest()[:10] + '.jpeg', 'wb') as file:
                # file.write(response.content)
                image.save(imagename, "JPEG", quality=100)

        print('Download Completed!')

    download_images(j.capitalize(), j, id_r)


def executeThread_a(i, j, id_r):
    print("thread", i)

    def download_images(data, Image_Folder, id_r):
        imagelinks = []
        num_images = 500
        count = 1

        print('Searching Images ' + data + '....')

        while len(imagelinks) < num_images and count < 45:
            count = count + 1
            print(count)

            search_url = "https://www.istockphoto.com/fr/search/2/image?mediatype=photography&page=" + str(
                count) + "&phrase=animaux%2520" + str(data).replace(" ", "%2520")
            

            response = requests.get(search_url)
            html = response.text

            b_soup = BeautifulSoup(html, 'html.parser')
            results = b_soup.findAll('figure', {'class': 'MosiacAsset-module__figure___1gQVb'})

            for res in results:
                if res.find('img').get('src') is None:
                    imagelinks.append(res.find('img').get('data-src'))
                else:
                    imagelinks.append(res.find('img').get('src'))

        # print(f'Found {len(imagelinks)} images')
        print('Start downloading...')

        for i, imagelink in enumerate(imagelinks):

            response = requests.get(imagelink).content

            image_file = io.BytesIO(response)
            image = Image.open(image_file).convert('RGB')

            color = "0"
            if (id_r == 2):
                color = "2"
            elif (id_r == 3):
                color = "4"
            elif (id_r == 4):
                color = "4"
            elif (id_r == 5):
                color = "3"
            elif (id_r == 6):
                color = "1"

            imagename = str(id_r) + "_0_" + color + "_" + str(i + 1) + '.jpg'

            with open(hashlib.sha1(response).hexdigest()[:10] + '.jpeg', 'wb') as file:
                # file.write(response.content)
                image.save(imagename, "JPEG", quality=100)

        print('Download Completed!')

    download_images(j.capitalize(), j, id_r)


os.chdir("D:\\_Projet Fin Année\\IA_finalTest2\\"+params().dataset_folder_name()+"\\")
threads = []
for id_r, j in test_races().items():
    thread = threading.Thread(target=executeThread_r, args=([i for i, x in enumerate(test_races()) if x == j], j, id_r))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()


threads = []
for id_r, j in test_animals().items():
    thread = threading.Thread(target=executeThread_a, args=([i for i, x in enumerate(test_animals()) if x == j], j, id_r))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()
