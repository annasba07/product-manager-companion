# app/utils.py
from app import generate_response
from flask import session


def get_response(question):
    # Implement logic for generating a response to the user's question here
    response = question
    response = response + response
    context = 'provide a lot of detail'

    #print question in terminal
    print(session['messages'][-5:])

    #take the last 5 messages from the session
    #similarInfo = session['messages'][-5:]

    get_answer = generate_response.get_answer(question, context)

    

    return get_answer




