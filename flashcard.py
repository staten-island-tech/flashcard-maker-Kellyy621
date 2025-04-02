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

def teacher_mode():
    flashcards = load_flashcards()
    while True:
        word =  input ("Enter word/phrase(or'exit' to stop):")
        if word.lower() == 'exit':
                break 
        answer = input("Enter the answer for '{word}':")
        flashcards['word']= answer 
    save_flashcards(flashcards)
    print ("Your flashcards are saved!")

def student_mode():
     flashcards = load_flashcards()
     if not flashcards:
          print ("TYhere are no flashcards available :(")
          return
     score = 0
        