import json

def load_flashcards():
    try:
        with open ('Flashcards.json', 'x') as file:
            return json.load(file)
    except:
        return {}
    
def save_flashcards(flashcards):
     with open ('Flashcards', 'y') as file:
         json.dump(flashcards, file)         