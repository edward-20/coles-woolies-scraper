"""
Scraping script
"""
from playwright.sync_api import sync_playwright

def main():
    """
    Main for Coles and Woolies Scraper
    """

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.coles.com.au/browse/down-down")
        print(page.title())
        browser.close()

    '''
    soup = BeautifulSoup(html, response.text)
    soup.find("h1")
    '''

    return 0

if __name__ == "__main__":
    main()
