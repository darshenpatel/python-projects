import re
from typing import Final

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Browser:
    def __init__(self):
        print('Starting up browser...')
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--disable-gpu')

        print('Installing ChromeDriver...')
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        print('ChromeDriver installed successfully.')

    def scrape_emails(self, url: str) -> set: ## `set` allows you to remove duplicates
        print(f'Scraping: "{url}" for emails')
        self.browser.get(url)
        page_source: str = self.browser.page_source

        list_of_emails = set()
        for regex_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(regex_match.group())
        return list_of_emails

    def close_browser(self):
        print('Closing the browser...')
        self.browser.quit()


def main():
    browser = None
    try:
        browser = Browser()
        emails: set = browser.scrape_emails('https://www.randomlists.com/email-addresses?qty=400')

        for i, email in enumerate(emails, start=1):
            print(i, email, sep=': ')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        if browser:
            browser.close_browser()


if __name__ == '__main__':
    main()


# Potential add-ons
    # 1. Come up with an error state if the browser page cannot be scraped.
    # 2. Come up with a way to scrape phone numbers -- can replicate the REGEX and scrape_emails function and specify to phone numbers.