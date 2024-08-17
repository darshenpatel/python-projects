import os
import requests

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    for ext in extensions:
        if ext in image_url:
            return ext

def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name = str = f'{folder}/{name}{ext}'
        else:
            image_name = str = f'{name}{ext}'
    else:
        raise Exception('Image extension is not supported')

    if os.path.isfile(image_name):
        raise Exception(f'File {image_name} already exists')


    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded {image_name} successfully!')
    except Exception as e:
        print(f'Error: {e}')


def main():
    input_url: str = input('Enter a url: ')
    input_name: str = input('Enter a name: ')
    download_image(input_url, name=input_name, folder='images')

if __name__ == '__main__':
    main()
    print('Downloading...')

# Potential add-ons
  # 1. List of image URLs and loop through them
  # 2. Name them automatically