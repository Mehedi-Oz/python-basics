"""
Create a program capable of displaying questions to the user like KBC.
Use List data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.
"""

# questions = [
#     "Q1: Is Python code compiled or interpreted?",
#     "Q2: All keywords in Python are in _________",
#     "Q3: Which keyword is used for function in Python language?",
# ]

# answers = [
#     # first Question's Probable Answers:
#     "a) Python code is both compiled and interpreted",
#     "b) Python code is neither compiled nor interpreted",
#     "c) Python code is only compiled",
#     "d) Python code is only interpreted",
#     # first Question's Answer:
#     "a) Python code is both compiled and interpreted",
#     # Second Question's Probable Answers:
#     "a) Capitalized",
#     "b) lower case",
#     "c) UPPER CASE",
#     "d) None of the mentioned",
#     # Second Question's Answer:
#     "d) None of the mentioned",
#     # Third Question's Probable Answers:
#     "a) Function",
#     "b) def",
#     "c) Fun",
#     "d) Define",
#     # Third Question's Answer:
#     "b) def",
# ]

# money = [5000, 10000, 20000, 40000, 80000, 160000]
# earned_money = 0
# answer_counter = 0

# for i in range(len(questions)):
#     print(f"\n{questions[i]}")

#     start_index = i * 5

#     for option_num in range(4):
#         print(answers[start_index + option_num])

#     answer_from_user = input("Answer: ")

#     if answer_from_user == answers[start_index + 4]:
#         earned_money = money[i]
#         print(f"Correct Answer!")
#         print(f"You've Earned {earned_money} Taka")
#         answer_counter += 1
#     else:
#         print(f"Sorry Wrong Answer!")
#         print(f"You've Earned {earned_money} Taka")
#         break


"""
OPTIMIZED SOLUTION
"""

# Simplified data structure - each question is a dictionary
questions = [
    {
        "question": "Q1: Is Python code compiled or interpreted?",
        "options": [
            "a) Python code is both compiled and interpreted",
            "b) Python code is neither compiled nor interpreted",
            "c) Python code is only compiled",
            "d) Python code is only interpreted",
        ],
        "answer": "a",
    },
    {
        "question": "Q2: All keywords in Python are in _________",
        "options": [
            "a) Capitalized",
            "b) lower case",
            "c) UPPER CASE",
            "d) None of the mentioned",
        ],
        "answer": "d",
    },
    {
        "question": "Q3: Which keyword is used for function in Python language?",
        "options": ["a) Function", "b) def", "c) Fun", "d) Define"],
        "answer": "b",
    },
]

# Prize money for each level
prize_money = [5000, 10000, 20000]
earned_money = 0

print("🎯 Welcome to KBC 🎯\n")

# Main game loop
for i, q in enumerate(questions):
    print(f"{q['question']}")
    print("-" * 50)

    # Display options
    for option in q["options"]:
        print(option)

    # Get user input
    user_answer = input("\nYour answer (a/b/c/d): ").lower().strip()

    # Check answer
    if user_answer == q["answer"]:
        earned_money = prize_money[i]
        print(f"✅ Correct! You've earned {earned_money} Taka!")
        print(f"💰 Current winnings: {earned_money} Taka\n")
    else:
        print(f"❌ Wrong answer! The correct answer was '{q['answer']}'")
        print(f"💰 Final amount: {earned_money} Taka")
        break
else:
    # This runs if loop completes without break
    print("🎉 Congratulations! You answered all questions correctly!")

print(f"\n🏆 Game Over! You're taking home: {earned_money} Taka")


print(type(questions))
