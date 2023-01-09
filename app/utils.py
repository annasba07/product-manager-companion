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
    similarInfo = session['messages']

    for i in similarInfo:
        context.append("Q: " + i + " A: ")

    #take the last 6 message and join them together by saying one message is "Q: " and the other is "A: "
    context = "Q: " + similarInfo[0] + " A: " + similarInfo[1] + " Q: " + similarInfo[2] + " A: " + similarInfo[3] + " Q: " + similarInfo[4] + " A: " + similarInfo[5]
    print(context)

    #for every item in similarinfo add it to the context
    
   

    get_answer = generate_response.get_answer(question, context)

    return get_answer




