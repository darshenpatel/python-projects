from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes = request.content

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.findAll('h2', class_='sc-4fedabc7-3 zTZri'):
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
    terms_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate (headlines, start=1):
        if term.lower() in headline:
            terms_found +=1
            terms_list.append(headline)
            print(f'{i}: {headline.capitalize()} <-- "{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('----------------------------------')
    if terms_found:
        print(f'"{term}" was mentioned {terms_found} times.')
        print('----------------------------------')

        for i, headline in enumerate(terms_list, start=1):
            print(f'{i}: {headline.capitalize()}')
    else:
        print(f'No matches found for: "{term}"')
        print('----------------------------------')


def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    user_input: str = input('What term would you like to check for? ')
    check_headlines(headlines, user_input)


if __name__ == '__main__':
    main()


# Potential add-ons
  # 1. Exact search term and not relative. Example, "ai"
  # 2. Make it much more accurate for search terms.