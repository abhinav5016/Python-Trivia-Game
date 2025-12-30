import random
from data.questions import python_questions



# Quiz function
def python_trivia_game(topic):
    print("Welcome to the Trivia Game!")

    question_dict = python_questions[topic]
    question_list = list(question_dict.items())
    random.shuffle(question_list)
    total_questions = 10
    score = 0

    print(f"\n---{topic.upper()} QUIZ ---\n")

    for idx, (question, correct_answer) in enumerate(question_list[:total_questions]):
        print(f"{idx + 1}. {question}")

        user_answer = input("Your answer: ").lower().strip()

        # stop game
        if user_answer == "exit":
            print("Game stopped. Thankyou!.")
            break

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong!. The correct Answer is: {correct_answer}.\n")

    print(f"Game Over! Your final score is: {score}/{total_questions}\n")


# Main Game loop
topics_list = list(python_questions.keys())

while True:
    print("Welcome to the Trivia Game!")
    print("Choose a Topic: ")
    for i, t in enumerate(topics_list, 1):
        print(f"{i}. {t.capitalize()}")

    user_choice = (
        input("Enter a topic number or name from the list above: ").lower().strip()
    )

    # If user enter number
    if user_choice.isdigit():
        num = int(user_choice)
        if 1 <= num <= len(topics_list):
            topic = topics_list[num - 1]
        else:
            print("Invalid number. Try again.\n")
            continue

    # If user enter topic name
    else:
        matched_topics = [t for t in topics_list if t.lower() == user_choice]
        if matched_topics:
            topic = matched_topics[0]
        else:
            print("Invalid number. Try again.\n")
            continue

    # run quiz
    python_trivia_game(topic)

    # Play Again?
    again = input("Do you want to play again? (yes/no): ").lower().strip()
    if again != "yes":
        print("Okay! Thankyou.")
        break
