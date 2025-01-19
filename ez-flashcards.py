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
                print(f"Wrong! The correct answer was: {correct_answer}")
        except ValueError:
            print(f"Invalid input! The correct answer was: {correct_answer}")

    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")

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
                print(f"Wrong! The correct answer was: {correct_answer}")
        except ValueError:
            print(f"Invalid input! The correct answer was: {correct_answer}")

    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")

def main():
    flashcards = load_flashcards("flashcards.json")

    print("Choose quiz mode:")
    print("1. Match question to answer (default mode)")
    print("2. Match answer to question (reverse mode)")
    
    mode = input("Enter 1 or 2: ").strip()
    
    if mode == "2":
        value_to_key_quiz(flashcards)
    else:
        key_to_value_quiz(flashcards)

# Run the main program
if __name__ == "__main__":
    main()
