# app/routes.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import utils

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/chat')
def chat():
    topic = request.args.get('topic')
    messages = []
    return render_template('chat.html', topic=topic, messages=messages)




@bp.route('/questions', methods=['POST'])
def questions(messages):
    question = request.form['question']
    response = utils.get_response(question)
    messages.append(question)
    messages.append(response)
    return redirect(url_for('routes.chat'))
