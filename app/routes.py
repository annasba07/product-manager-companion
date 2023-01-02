# app/routes.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
import json
from app import utils

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')




@bp.route('/chat', methods=['GET', 'POST'])
def chat():
    topic = request.args.get('topic')
    messages = request.args.get('messages', [])
    if request.method == 'POST':
        question = request.form['question']
        messages = json.loads(request.form['messages'])
        response = utils.get_response(question)
        messages.append(question)
        messages.append(response)
    return render_template('chat.html', topic=topic, messages=messages)






@bp.route('/questions', methods=['POST'])
def questions():
    question = request.form['question']
    messages = json.loads(request.form['messages'])
    response = utils.get_response(question)
    messages.append(question)
    messages.append(response)
    return redirect(url_for('routes.chat'))
