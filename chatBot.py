from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You:')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print(f'Bot: I do not understand...')


if __name__ == '__main__':
    brain: dict = {'Hello': 'Hey There!',
                   'How are you?': 'I am good, thanks!',
                   'Bye': 'See you later!'}

    chat_bot(knowledge=brain)

# Potential add-ons
  # 1. Load JSON file for dictionary
  # 2. Function for date and time