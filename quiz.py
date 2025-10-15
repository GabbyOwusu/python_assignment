quiz_questions = [
    {
        "question": "Who is the president of Ghana?",
        "options": [
            "A. John Dramani Mahama",
            "B. Nana Akufo-Addo",
            "C. Rawlings",
            "D. Kufuor"
        ],
        "correct_answer": "A",
        "user_input": "",
        "explanation": "Nana Akufo-Addo is the president of Ghana."
    },
    {
        "question": "What is the capital of Ghana?",
        "options": [
            "A. Accra",
            "B. Kumasi",
            "C. Takoradi",
            "D. Tamale"
        ],
        "correct_answer": "A",
        "user_input": "",
        "explanation": "Accra is the capital of Ghana."
    },
    {
        "question": "When did Ghana gain independence?",
        "options": [
            "A. 1999",
            "B. 1957",
            "C. 1866",
            "D. 1910"
        ],
        "user_input": "",
        "correct_answer": "B",
        "explanation": "Ghana gained independence in 1957",
    },
    {
        "question": "Who helped Ghana gain independence?",
        "options": [
            "A. H.E Jerry John Rawlings",
            "B. Otumfuor Osei Tutu",
            "C. Dr. Osagyefo Kwame Nkrumah",
            "D. H.E John Agyekum Kuffuor",
        ],
        "user_input": "",
        "correct_answer": "C",
        "explanation": "Dr. Osagyefo Kwame Nkrumah gained independence for Ghana",
    },
    {
        "question": "Who is the current finance minister",
        "options": [
            "A. Hon. Ato Forson",
            "B. Hon. Aban Gbagbin",
            "C. Hon. Ken Ofori Attah",
            "D. Mrs. Samira Bawumia",
        ],
        "user_input": "",
        "correct_answer": "A",
        "explanation": "Hon. Ato Forson is the current finance minister for Ghana",
    }
]


questions_length = len(quiz_questions)
current_index = 0


def handleNumberOfCorrectAnswers():
    number_of_correct_items = 0

    for item in quiz_questions:
        if item['user_input'] == "correct":
            number_of_correct_items += 1
        else:
            continue
    result_percentage = (number_of_correct_items / questions_length) * 100
    print(
        f'\nYour overral score is {result_percentage}%'
        f'\nYou got {number_of_correct_items} out of {questions_length} answers correct\n'
    )


def handleQuizQuestions():
    global current_index

    if current_index == questions_length:
        handleNumberOfCorrectAnswers()
        return
    current_question = quiz_questions[current_index]
    user_input = input(
        f"\n{current_question['question']}\n{"\n".join(current_question["options"])}\n"
        "Select the alphabet that matches your answer: "
    )
    current_question['user_input'] = user_input
    if user_input == current_question['correct_answer']:
        quiz_questions[current_index]['user_input'] = "correct"
        print('✅ Thats a correct answer! Keep going!')
    else:
        quiz_questions[current_index]['user_input'] = "wrong"
        print(
            f'❌ Thats wrong. The correct answer is "{current_question["correct_answer"]}"\n{current_question["explanation"]}\n\n')
    current_index += 1
    return handleQuizQuestions()


handleQuizQuestions()
