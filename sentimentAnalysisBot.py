from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input: str, *, sensitivity: float) -> Mood: ## The asterisk forces the use of the parameter, "sensitivity."
    polarity: float = TextBlob(input).sentiment.polarity

    friendly_threshold: float = sensitivity
    unfriendly_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('😃', polarity)
    elif polarity <= unfriendly_threshold:
        return Mood('☹️', polarity)
    else:
        return Mood('😐', polarity)

def run_bot():
    print('Enter your mood:')
    while True:
        user_input: str = input ('You:')
        mood: Mood = get_mood(user_input, sensitivity=0.3) # 0.1 = super sensitive, 0.9 = least sensitive.
        print(f'Bot: {mood.emoji} ({mood.sentiment})')

if __name__ == '__main__':
    run_bot()



