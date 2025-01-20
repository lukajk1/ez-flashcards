import json
import random

def load_flashcards(filename):
    with open(filename, "r") as file:
        return json.load(file)

def create_options(correct_answer, all_answers):
    options = set([correct_answer])
    while len(options) < 4:
        options.add(random.choice(all_answers))
    return list(options)

def key_to_value_quiz(flashcards):
    questions = list(flashcards.keys())
    all_answers = list(flashcards.values())
    random.shuffle(questions)

    score = 0

    for question in questions:
        correct_answer = flashcards[question]
        options = create_options(correct_answer, all_answers)
        random.shuffle(options)

        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Your choice (1-4): "))
            if 1 <= choice <= 4 and options[choice - 1] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The answer was: {correct_answer}")
        except ValueError:
            print(f"Invalid input - the correct answer was: {correct_answer}")

    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")
    main_prompt(flashcards)

def value_to_key_quiz(flashcards):
    reversed_flashcards = {v: k for k, v in flashcards.items()}
    questions = list(reversed_flashcards.keys())
    all_answers = list(reversed_flashcards.values())
    random.shuffle(questions)

    score = 0

    for question in questions:
        correct_answer = reversed_flashcards[question]
        options = create_options(correct_answer, all_answers)
        random.shuffle(options)

        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Your choice (1-4): "))
            if 1 <= choice <= 4 and options[choice - 1] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The answer was: {correct_answer}")
        except ValueError:
            print(f"Invalid input - the answer was: {correct_answer}")

    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")
    main_prompt(flashcards)

def front_to_back(flashcards):
    questions = list(flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        print(f"\nFront: {question}")
        input("Press any key to reveal the back...")
        print(f"Back: {flashcards[question]}")

    print("\nFlashcard review complete!")
    main_prompt(flashcards)

def back_to_front(flashcards):
    reversed_flashcards = {v: k for k, v in flashcards.items()}
    questions = list(reversed_flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        print(f"\nBack: {question}")
        input("Press any key to reveal the front...")
        print(f"Front: {reversed_flashcards[question]}")

    print("\nFlashcard review complete!")
    main_prompt(flashcards)

def main_prompt(flashcards):
    print("Choose mode:")
    print("1. classic flashcard")
    print("2. reverse classic flashcard")
    print("3. quiz")
    print("4. reverse quiz")
    print()
    
    response = input("Enter 1, 2, 3, or 4: ").strip()

    match response:
        case "1":
            front_to_back(flashcards)
        case "2":
            back_to_front(flashcards)
        case "3":
            key_to_value_quiz(flashcards)
        case "4":
            value_to_key_quiz(flashcards)
        case _:
            print("Invalid input!")
            main_prompt(flashcards)
            
def main():
    try:
        flashcards = load_flashcards("flashcards.json")
        main_prompt(flashcards)
    except FileNotFoundError:
        print("Error: 'flashcards.json' file not found. Please ensure the file exists in the current directory.")

if __name__ == "__main__":
    print("ez-flashcards :D v1.1r")
    print()
    main()
