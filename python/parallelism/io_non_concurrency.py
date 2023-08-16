import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    # Session object allows one to persist certain parameters across requests.
    # It also persists cookies across all requests made from the Session instance and will use urllib3’s connection pooling.
    # So, if several requests are being made to the same host, the underlying TCP connection will be reused,
    # which can result in a significant performance increase.
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    # Downloaded 160 in 12.654400825500488 seconds
