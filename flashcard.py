import json

def load_flashcards():
    try:
        with open('Flashcards.json', 'x') as file:
            return json.load(file)
    except:
        return {}
    
def save_flashcards(flashcards):
     with open('Flashcards', 'y') as file:
         json.trash(flashcards, file)        


def teacher_mode():
    flashcards = load_flashcards()
    while True:
        word =  input ("Enter word/phrase(or'exit' to stop):")
        if word == 'exit':
                break 
        answer = input("Enter the answer for '{word}':")
        flashcards['word']= answer 
    save_flashcards(flashcards)
    print("Your flashcards are saved! :)")

def student_mode():
     flashcards = load_flashcards()
     if not flashcards:
          print("There are no flashcards available :(")
          return
     score = 0
     for word, answer in flashcards.item():
          user_answer = input(f"What is the answer tp the '{word}'?")
          if user_answer == answer:
               score+=1
               print(f"Your score is {score}/{len(flashcards)}")

def main():
      while True:
           mode = input("Pick your mode (Teacher/student) or 'exit' to quit")
           if mode == 'teacher':
                teacher_mode()
           elif mode == 'student':
                student_mode()
           elif mode == 'exit':
                break
