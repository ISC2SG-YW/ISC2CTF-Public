from flask import Flask, render_template, request, redirect, url_for, session
import random
import time

app = Flask(__name__)
app.secret_key = 'ilooooooooovechonkycats'  # Necessary for session management

def load_equations():
    equations = {}
    with open('equation_answers.txt', 'r') as file:
        for line in file:
            id, answer = line.strip().split(', ')
            equations[id] = answer
    return equations

equations = load_equations()

@app.route('/')
def index():
    session['score'] = 0
    session['answered_questions'] = []
    return redirect(url_for('next_question'))

@app.route('/question')
def next_question():
    if session['score'] == 49:
        return render_template('flag.html', flag="ISC2CTF{d3n01sing_r41nb0w_no1s3_1s_4_gRE4t_1d34}")
    
    question_id = random.choice(list(equations.keys()))
    session['current_question'] = question_id
    session['start_time'] = time.time()  # Reset the timer for this question

    return render_template('question.html', question_id=question_id)

@app.route('/answer', methods=['POST'])
def answer():
    if 'current_question' not in session:
        return redirect(url_for('next_question'))

    elapsed_time = time.time() - session['start_time']
    if elapsed_time > 5:
        session['score'] = 0  # reset score if the time limit is exceeded
        return redirect(url_for('index'))  # restart quiz

    answer = request.form['answer']
    question_id = session['current_question']
    correct_answer = equations[question_id]

    if answer == correct_answer:
        session['score'] += 1
        session['answered_questions'].append(question_id)
        if session['score'] == 50:
            return redirect(url_for('index'))
        return redirect(url_for('next_question'))
    else:
        session['score'] = 0  # reset score if the answer is wrong
        return redirect(url_for('index'))  # restart quiz


@app.route('/static/images/<filename>')
def serve_image(filename):
    return app.send_static_file(f'images/{filename}')

if __name__ == '__main__':
    app.run()
