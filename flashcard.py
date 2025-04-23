import json

def load_flashcards():
     try:
        with open('Flashcards.json', 'r') as file:
            return json.load(file)
     except FileNotFoundError:
        return {}
def save_flashcards(flashcards):
     with open('Flashcards.json', 'w') as file:
         json.dump(flashcards, file)  

flashcards = {
     "An apple a day keeps the doctor away":"Famous saying",
     "Mean girls":"Highschool movie",
     "Peppa pig":"kids show"
} 

def main():
     while True:
         mode = input("Pick your mode (Teacher/student) or 'exit' to quit")
         if mode == 'teacher':
               teacher_mode()
         elif mode == 'student':
               student_mode()
         elif mode == 'exit':
               break

def teacher_mode():
    flashcards = load_flashcards()
    while True:
        word =  input ("Enter word/phrase(or'exit' to stop):")
        if word == 'exit':
                break 
        answer = input("Enter the answer for '{word}':")
        flashcards[word]= answer 
    save_flashcards(flashcards)
    print("Your flashcards are saved! :)")

def student_mode():
     flashcards = load_flashcards()
     print("Loaded flashcards in student mode:", flashcards)

     if not flashcards:
          print("There are no flashcards available :(")
          return
     
     score = 0
     for word, answer in flashcards.items():
          user_answer = input(f"What is the answer to the '{word}'?")
          if user_answer == answer:
               score+=1
               print(f"Correct, your score is {score}/{len(flashcards)}!") #len counts the number of flashcards 
          else:
               print(f"Wrong, the correct answer is: {word}")

     print(f"Your final score is {score}/{len(flashcards)}") #amount right/amount of flashcards
  
