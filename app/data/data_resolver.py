from downloader import Downloader


def main():
    dl = Downloader()
    dl.get_wp()
    print("wp fetched")
    a = dl.get_news()
    print("news links extracted")
    print(a)


if __name__ == '__main__':
    main()
