# app/utils.py
from app import generate_response
from flask import session


def get_response(question):
    # Implement logic for generating a response to the user's question here
    response = question
    response = response + response
    context = 'provide a lot of detail'

    #print question in terminal
    print(session['messages'][-6:])

    #take the last 5 messages from the session
    similarInfo = session['messages'][-6:]

    #take the last 6 message and join them together by saying one message is "Q: " and the other is "A: "
    context = "Q: " + similarInfo[0] + " A: " + similarInfo[1] + " Q: " + similarInfo[2] + " A: " + similarInfo[3] + " Q: " + similarInfo[4] + " A: " + similarInfo[5]
    print(context)

    #take the last 6 messages and join them together by saying one message is "Q: " and the other is "A: " if there are less than 6 messages, then just use the messages that are there
    if len(similarInfo) < 6:
        context = "Q: " + similarInfo[0] + " A: " + similarInfo[1] + " Q: " + similarInfo[2] + " A: " + similarInfo[3] + " Q: " + similarInfo[4] + " A: " + similarInfo[5]

    get_answer = generate_response.get_answer(question, context)

    return get_answer




