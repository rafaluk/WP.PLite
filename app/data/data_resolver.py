from app.data.downloader import Downloader


def wp():
    dl = Downloader()
    dl.get_wp()
    print("wp fetched")
    links = dl.get_news()
    print("news links extracted")
    return links

#
# if __name__ == '__main__':
#     main()
