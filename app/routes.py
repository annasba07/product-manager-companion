# app/routes.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
import json
from flask import Flask
from app import utils
from flask import session

import logging

bp = Blueprint('routes', __name__)

app = Flask(__name__)
logger = logging.getLogger(__name__)

@bp.route('/')
def index():
    return render_template('index.html')




@bp.route('/chat', methods=['GET', 'POST'])
def chat():
    topic = request.args.get('topic')
    #messages = request.args.get('messages', [])
    messages = session.get('messages', [])
    
    if request.method == 'POST':
        question = request.form['question']
        #messages = request.form['messages']
        response = utils.get_response(question)
        messages = list(messages)
        #app.logger.warning(messages)
        #logger.info('This is an info message')
        messages.append(question)
        messages.append(response)
        session['messages'] = messages
    return render_template('chat.html', topic=topic, messages=messages)






@bp.route('/questions', methods=['POST'])
def questions():
    question = request.form['question']
    messages = json.loads(request.form['messages'])
    response = utils.get_response(question)
    messages.append(question)
    messages.append(response)
    return redirect(url_for('routes.chat'))

