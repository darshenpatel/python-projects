from random import choice

def run_game():
    word: str = choice (['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
                         'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power',
                         'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism',
                         'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider',
                         'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language',
                         'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus',
                         'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
                         'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard',
                         'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
                         'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
                         'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
                         'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
                         'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph',
                         'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower',
                         'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'wind',
                         'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive'
                         'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure',
                         'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter',
                         'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy',
                         'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 'friend',
                         'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 'basketball',
                         'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment',
                         'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion',
                         'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 'expectation',
                         'absence', 'mystery', 'morning', 'device', 'thoughts', 'spirit', 'future',
                         'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection',
                         'achievement', 'lightning', 'secret', 'environment', 'shepherd', 'confusion',
                         'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn',
                         'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment',
                         'permission', 'logic', 'analysis', 'password', 'english', 'equalizer',
                         'emotion', 'battle', 'expression', 'scissors', 'trousers', 'glasses', 'department',
                         'dictionary', 'chemistry', 'induction', 'detail', 'widow', 'wealth', 'health',
                         'disaster', 'volcano', 'poverty', 'limitation', 'perfect', 'intelligence',
                         'failure', 'ignorance', 'destination', 'source', 'resort', 'satisfaction', 'example',
                         'frequency', 'selection', 'substitution', 'kingdom', 'pattern', 'management',
                         'situation', 'multiply', 'treatment', 'dollar', 'intuition', 'chapter', 'magnet'
                         'desire', 'command', 'action', 'consciousness', 'enemy', 'security', 'object',
                         'happen', 'happiness', 'worry', 'method', 'tolerance', 'error', 'hesitation',
                         'record', 'tongue', 'supply', 'vibration', 'stress', 'despair', 'restaurant',
                         'television', 'video', 'audio', 'layer', 'mixture', 'doorbell', 'cousin', 'beard',
                         'finance', 'production', 'invisible', 'excitement', 'afternoon', 'office', 'alpha',
                         'illustration', 'valley', 'apartment', 'necessary', 'shortage', 'almost', 'furniture',
                         'blanket', 'suggestion', 'overflow', 'demonstration', 'challenge', 'compact',
                         'tower', 'question', 'problem', 'pressure', 'beast', 'encouragement', 'afraid',
                         'cavity', 'appearance', 'wonderful', 'matter', 'dimension', 'business', 'doubt',
                         'conversation', 'reaction', 'psychology', 'superstition', 'smash', 'horseshoe',
                         'surprise', 'nothing', 'ladder', 'opposite', 'reality', 'genius', 'string',
                         'destruction', 'expensive', 'painting', 'chicken', 'wishing', 'profession', 'engineer',
                         'hatred', 'possession', 'criticism', 'zebra', 'harmony', 'personality', 'overcome',
                         'addition', 'subtraction', 'cipher', 'encryption', 'compression', 'extension',
                         'blessing', 'meeting', 'difficulty', 'weapon', 'against', 'external', 'internal'
                         'legend', 'servant', 'secondary', 'license', 'directory', 'statistics',
                         'attraction', 'sensitivity', 'magnification', 'someone', 'symptom', 'recipe',
                         'service', 'family', 'island', 'planet', 'butterfly', 'diving', 'strength',
                         'extreme', 'opportunity', 'illumination', 'cable', 'conflict', 'interference',
                         'receiver', 'transmitter', 'channel', 'company', 'grocery', 'devil', 'angel',
                         'exactly', 'document', 'tutorial', 'sound', 'voice', 'abbreviation', 'abdomen',
                         'abrupt', 'absolute', 'absorption', 'abstract', 'academy', 'acceleration',
                         'accident', 'account', 'acidification', 'actress', 'adaptation', 'addiction',
                         'adjustment', 'admiration', 'adoption', 'advanced', 'adventure', 'advertisement'
                         'agenda', 'airport', 'algorithm', 'allocation', 'aluminium', 'ambiguity',
                         'amphibian', 'anaesthesia', 'analogy', 'anchor', 'animation', 'anode', 'cathode'
                         'apparent', 'appendix', 'approval', 'approximation', 'arbitrary', 'architecture'
                         'arithmetic', 'arrangement', 'article', 'ascending', 'ashamed', 'asleep',
                         'assembly', 'astonishment', 'atmosphere', 'awful', 'bachelor', 'backbone',
                         'bacteria', 'balance', 'balloon', 'banana', 'barbecue', 'baseball', 'beaker',
                         'beggar', 'behaviour', 'benefit', 'bidirectional', 'biology', 'blackboard',
                         'bladder', 'bleeding', 'blender', 'bonus', 'bottle', 'bracket', 'branch',
                         'bubble', 'bucket', 'budget', 'bullet', 'burglar', 'butcher', 'bypass',
                         'calculator', 'calibration', 'campaign', 'cancellation', 'candidate', 'candle',
                         'carpenter', 'carriage', 'cartoon', 'cascade', 'casual', 'catalyst', 'category',
                         'cement', 'ceremony', 'chairman', 'checkout', 'chimney', 'chocolate',
                         'circumference', 'civilization', 'classroom', 'clearance', 'client', 'coconut',
                         'coincidence', 'colleague', 'comfortable', 'competition', 'kangaroo', 'kidnap',
                         'journal', 'jockey', 'iteration', 'isometric', 'isolation', 'invitation',
                         'institution', 'injection', 'humanity', 'housekeeper', 'history', 'heaven',
                         'greenhouse', 'glory', 'foundation', 'formula', 'fluctuation', 'fiction',
                         'emission', 'elasticity', 'earthquake', 'dynamic', 'doctorate', 'divorce', 'nightmare',
                         'virtue', 'description'])

    username: str = input('What is your name? ')
    print(f'Welcome to hangman, {username}!')

    #Setup
    guessed: str = ''
    tries: int = 4

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for character in word:
            if character in guessed:
                print(character, end='')
            else:
                print('_', end='')
                blanks+=1

        print()  #Adds a blank line

        if blanks == 0:
            print('You have guessed the word!')
            break

        guess: str = input('Guess a letter: ')

        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong, you have {tries} tries remaining')

            if tries == 0:
                print ('No more tries remaining. You lose the game!')
                break


if __name__ == '__main__':
    run_game()


# Potential add-ons
  # 1.Give the word if you run out of guesses
  # 2. Type in all the letters at once to guess the word
  # 3. Do not cheat by typing in all the letters to fill in the blanks. It should still be one at a time.