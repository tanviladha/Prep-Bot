#This chatbot was constructed with help from the tutorial by Indently which can be found here:
#https://www.youtube.com/watch?v=CkkjXTER2KE

import json
#https://docs.python.org/3/library/difflib.html
from difflib import get_close_matches

#Load the knowledge base into the program
def load_knowledgebase(file_path: str) -> dict:
    #open file from file_path in read mode
    with open(file_path, 'r') as file:
        #data of type dictionary is going to equal the json file
        data: dict = json.load(file)
    return data

#Saving the knowledge base to ensure that the next time the program runs it has the old responses still stored
def save_knowledgebase(file_path: str, data: dict):
    #opens in write mode
    with open(file_path, 'w') as file:
        #puts dictionary of responses back into the json file
        json.dump(data, file, indent=2)

#This function helps the chatbot find the best response to the users question
def find_best_response(user_question: str, questions: list[str]) -> str | None:
    #uses the imported get_close_matches function
    #having an n = 1 makes it so that it will only return the first best match
    #cutoff is like an accuracy (60% accuracy/similar)
    matches: list = get_close_matches(user_question, questions, n=1, cutoff = 0.6)
    return matches[0] if matches else None

def get_answer(question: str, knowledgebase: dict) -> str | None:
    for q in knowledgebase["questions"]:
        if q["question"] == question:
            return q["answer"]

def run_chatbot():
    knowledgebase: dict = load_knowledgebase("knowledgebase.json")

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_response: str | None = find_best_response(user_input, [q["question"] for q in knowledgebase["questions"]])

        if best_response:
            answer: str = get_answer(best_response, knowledgebase)
            print(f'Bot: {answer}')
        else:
            print('Sorry, I don\'t know the answer. Will you teach me?')
            new_answer: str = input('Type the answer or type \'skip\' to skip. ')

            if new_answer.lower() != 'skip':
                knowledgebase["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledgebase('knowledgebase.json', knowledgebase)
                print('Bot: Thank you for teaching me!')


if __name__ == '__main__':
    run_chatbot()