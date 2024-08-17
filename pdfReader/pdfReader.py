import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        # Include the strict parameter if it's supported by your version of PyPDF2
        try:
            reader = PdfReader(pdf, strict=False)
        except TypeError:
            reader = PdfReader(pdf)

        print('Pages:', len(reader.pages))
        print('-' * 10)  # Divider

        pdf_text = [page.extract_text() for page in reader.pages if page.extract_text() is not None]
        return pdf_text


def count_words (text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())

        all_words += [word for word in split_text if word]

    return Counter(all_words)


def main():
    extracted_text: list[str] = extract_text('DeepLearning_AI-Playbook_v6.pdf')
    counter: Counter = count_words(text_list=extracted_text)

    for page in extracted_text:
        print(page)

    for word, mentions in counter.most_common(5):
        print(f'{word:5}: {mentions} times')


if __name__ == '__main__':
    main()