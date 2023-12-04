def create_flashcard(category, question, answer):
    flashcard = f"Category: {category}\nQuestion: {question}\nAnswer: {answer}\n"
    return flashcard

def save_flashcards_to_file(flashcards, filename):
    with open(filename, 'a') as file:
        for card in flashcards:
            file.write(card)
            file.write('\n')

def load_flashcards_from_file(filename):
    flashcards = []
    with open(filename, 'r') as file:
        flashcard = {}
        for line in file:
            line = line.strip()
            if line.startswith("Category:"):
                if flashcard:
                    flashcards.append(flashcard)
                flashcard = {'Category': line.split(":")[1].strip()}
            elif line.startswith("Question:"):
                flashcard['Question'] = line.split(":")[1].strip()
            elif line.startswith("Answer:"):
                flashcard['Answer'] = line.split(":")[1].strip()
        if flashcard:
            flashcards.append(flashcard)
    return flashcards

def quiz_flashcards(flashcards):
    for flashcard in flashcards:
        print("\nCategory:", flashcard['Category'])
        input("Press Enter to see the question...")
        print("Question:", flashcard['Question'])
        input("Press Enter to see the answer...")
        print("Answer:", flashcard['Answer'])
        input("Press Enter to continue to the next flashcard...")

def main():
    choice = input("Enter '1' to create flashcards or '2' to quiz yourself: ")

    if choice == '1':
        flashcards = []

        for _ in range(3):
            category = input("Enter the category (JavaScript, Mobile, or C#): ").capitalize()
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")

            flashcard = create_flashcard(category, question, answer)
            flashcards.append(flashcard)

        save_flashcards_to_file(flashcards, 'flashcards.txt')
        print("Flashcards created and saved.")

    elif choice == '2':
        loaded_flashcards = load_flashcards_from_file('flashcards.txt')
        quiz_flashcards(loaded_flashcards)

    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()