# app/utils.py
from app import generate_response
from flask import session


def get_response(question):
    # Implement logic for generating a response to the user's question here
    
    context = ''

    #print question in terminal
    print(session['messages'][-6:])

    #take the last 5 messages from the session
    similarInfo = session['messages']

 

    #take the last 6 message and join them together by saying one message is "Q: " and the other is "A: "
    if len(similarInfo) > 4:
        context = " A: " + similarInfo[-5] + "\n Q: " + similarInfo[-4] + "\n A: " + similarInfo[-3] + "\n Q: " + similarInfo[-2] + "\n A: " + similarInfo[-1]
    elif len(similarInfo) > 2:
        context = " A: " + similarInfo[-3] + "\n Q: " + similarInfo[-2] + "\n A: " + similarInfo[-1]
    elif len(similarInfo) > 0:
        context = " A: " + similarInfo[-1] 

   
    
   

    get_answer = generate_response.get_answer(question, context)

    return get_answer




