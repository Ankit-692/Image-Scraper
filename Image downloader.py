import bs4
import requests
import random



def search_img():
    search = input("What you want to search for: ")
    num = int(input("How many images you want to download (maximum = 80): "))
    print('Downloading....')
    print('Please wait..')
    if num <= 80:
        try:
            page = requests.get(f'https://www.wallpaperflare.com/search?wallpaper={search}')
            page_b4 = bs4.BeautifulSoup(page.text, 'lxml').select('img')
            if len(page_b4) != 1:
                download(page_b4, num + 1)
            else:
                print("Please use a valid keyword for search\n")
                search_img()
        except:
            print("check your internet connection and try again")
            search_img()

    else:
        print("Please keep the number less than 80")
        search_img()


def download(page_b4, num):
    random.shuffle(page_b4)
    for i in range(1, num):
        try:
            name = page_b4[i]['alt']
            link = page_b4[i].attrs['data-src']
            link_image = requests.get(link)
        except:
            pass
        else:
            f_open = open(f'Downloads/{name}.jpg', 'wb')
            f_open.write(link_image.content)
            f_open.close()


search_img()
