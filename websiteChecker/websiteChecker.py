import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1] or 'http://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
        return websites

def get_user_agents() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return 'Unknown Status Code...'

def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={'User Agent': user_agent}).status_code
        print(website, get_status(code))
    except Exception as e:
        print(f'Could not get the status of {website}: {e}')

def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_user_agents()

    for i, site in enumerate(sites):
        check_website(site, user_agent)

if __name__ == '__main__':
    main()