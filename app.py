import os
import json
import requests
from functools import wraps
from flask import (
    Flask, 
    send_from_directory, 
    redirect, 
    render_template, 
    request,
    session, 
    abort
)
import firebase_admin
from firebase_admin import credentials, firestore
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from google.oauth2 import id_token
import cachecontrol

if __name__ == '__main__':
    credSurvey = credentials.Certificate('survey.json')
    credTodo = credentials.Certificate('todo.json')
    credQuickNotes = credentials.Certificate('quicknotes.json')
else:
    credSurvey = credentials.Certificate('/home/JamesRFMathis/web-apps/survey.json')
    credTodo = credentials.Certificate('/home/JamesRFMathis/web-apps/todo.json')
    credQuickNotes = credentials.Certificate('/home/JamesRFMathis/web-apps/quicknotes.json')

firebase_admin.initialize_app(credSurvey, name='survey')
firebase_admin.initialize_app(credTodo, name='todo')
firebase_admin.initialize_app(credQuickNotes, name='quicknotes')

app = Flask(__name__, static_folder='static')

if __name__ == '__main__':
    app.secret_key = json.load(open('quicknotes-oauth.json', 'r'))['web']['client_secret']
    clientID = json.load(open('quicknotes-oauth.json', 'r'))['web']['client_id']

    flow = Flow.from_client_secrets_file(
        client_secrets_file='quicknotes-oauth.json',
        scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid'],
        redirect_uri='http://localhost:5000/assignment8/callback'
    )

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
else:
    app.secret_key = json.load(open('/home/JamesRFMathis/web-apps/quicknotes-oauth.json'))['web']['client_secret']
    clientID = json.load(open('/home/JamesRFMathis/web-apps/quicknotes-oauth.json'))['web']['client_id']

    flow = Flow.from_client_secrets_file(
        client_secrets_file='/home/JamesRFMathis/web-apps/quicknotes-oauth.json',
        scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid'],
        redirect_uri='http://jamesrfmathis.pythonanywhere.com/assignment8/callback'
    )

def loginRequired(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'sub' not in session:
            return redirect('/')
        else:
            return function()
    return wrapper

@app.route('/')
def home():
    return send_from_directory(app.static_folder + '/home/html', 'index.html')

@app.route('/hello')
def hello():
    name = 'Bob'
    if request.method == 'GET' and 'name' in request.args:
        name = request.args['name']
    return render_template('hello.html', name=name)

@app.route('/assignment1/bio')
def bio():
    return send_from_directory(app.static_folder + '/bio-site/html', 'bio.html')

@app.route('/assignment1/schedule')
def schedule():
    return send_from_directory(app.static_folder + '/bio-site/html', 'schedule.html')

@app.route('/assignment1/favorites')
def favorites():
    return send_from_directory(app.static_folder + '/bio-site/html', 'favorites.html')

@app.route('/assignment2/cringy-ss')
def cringy_ss():    
    return send_from_directory(app.static_folder + '/CringySS/html', 'cringyss.html')

@app.route('/assignment3/zen-garden')
def zen_garden():    
    return send_from_directory(app.static_folder + '/ZenGarden/html', 'index.html')

@app.route('/assignment4/quiz')
def quiz():
    if request.method == 'GET' and 'question' in request.args:
        question = request.args['question']
        name = request.args['name']

        if 'answer1' in request.args:
            answer1 = request.args['answer1']
        if 'answer2' in request.args:
            answer2 = request.args['answer2']
        if 'answer3' in request.args:
            answer3 = request.args['answer3']
        if 'answer4' in request.args:
            answer4 = request.args['answer4']
        if 'answer5' in request.args:
            answer5 = request.args['answer5']
    
        if question == '1':
            return render_template('quiz1.html', name=name)
        if question == '2':
            return render_template('quiz2.html', name=name, answer1=answer1)
        if question == '3':
            return render_template('quiz3.html', name=name, answer1=answer1, answer2=answer2)
        if question == '4':
            return render_template('quiz4.html', name=name, answer1=answer1, answer2=answer2, answer3=answer3)
        if question == '5':
            return render_template('quiz5.html', name=name, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4)
        if question == 'end':
            answers = [answer1, answer2, answer3, answer4, answer5]

            totalA = 0
            totalB = 0
            totalC = 0
            totalD = 0
            totalE = 0

            for answer in answers:
                if answer == 'A':
                    totalA += 1
                if answer == 'B':
                    totalB += 1
                if answer == 'C':
                    totalC += 1
                if answer == 'D':
                    totalD += 1
                if answer == 'E':
                    totalE += 1

            answersDict = {
                'A': totalA,
                'B': totalB,
                'C': totalC,
                'D': totalD,
                'E': totalE
            }

            result = max(answersDict, key=answersDict.get)

            if result == 'A':
                soulmate = 'Inquisitor Eisenhorn'
                desc = 'Inquisitor Gregor Eisenhorn is a dedicated servant of the Imperium, known for his unwavering commitment to rooting out heresy and investigating the darkest corners of the galaxy. He is a skilled investigator and psyker, leading a life of danger and intrigue.'
            if result == 'B':
                soulmate = 'Ahriman, Chief Librarian of the Thousand Sons'
                desc = 'Ahriman is a formidable and complex character, Chief Librarian of the Thousand Sons Legion. He wields immense psychic powers and is known for his relentless pursuit of knowledge and mastery over the arcane arts. Ahriman is a key figure in the lore of Chaos.'
            if result == 'C':
                soulmate = 'Typhus, Herald of Nurgle'
                desc = 'Typhus is a champion of Nurgle, the Plague God. He is a fearsome and grotesque figure known for spreading disease and decay across the galaxy. Typhus leads the Death Guard Legion in their relentless pursuit of spreading the blessings of Nurgle.'
            if result == 'D':
                soulmate = 'Commisar Yarrick'
                desc = ' Commissar Sebastian Yarrick is an iconic Imperial officer renowned for his unyielding determination and relentless pursuit of justice. He is a symbol of unwavering loyalty to the Imperium and is known for his feud with the Ork Warlord Ghazghkull Thraka.'
            if result == 'E':
                soulmate = 'Ork Warboss Ghazghkull Thraka'
                desc = 'Ghazghkull Thraka is a cunning and brutal Ork Warlord, known for his leadership of the Ork Waaagh! and his desire to conquer the galaxy. He\'s a powerful and iconic figure in the Ork culture, always seeking the next great fight and challenge.'

            return render_template('quizEnd.html', name=name, soulmate=soulmate, desc=desc)
    return send_from_directory(app.static_folder + '/Quiz', 'quiz.html')

@app.route('/assignment5/connect4')
def connect4():
    return send_from_directory(app.static_folder + '/Connect4/html', 'index.html')

@app.route('/assignment6/survey')
def survey():
    return send_from_directory(app.static_folder + '/Survey/html', 'index.html')

@app.route('/assignment6/survey/submit-survey', methods=['POST'])
def submit_survey():
    db = firestore.client(app=firebase_admin.get_app('survey'))

    print('submitting survey')
    vote = request.form['class']
    if vote == 'fighter':
        db.collection('votes').document('fighter').update({'votes': firestore.Increment(1)})
    elif vote == 'wizard':
        db.collection('votes').document('wizard').update({'votes': firestore.Increment(1)})
    elif vote == 'rogue':
        db.collection('votes').document('rogue').update({'votes': firestore.Increment(1)})
    elif vote == 'cleric':
        db.collection('votes').document('cleric').update({'votes': firestore.Increment(1)})

    return redirect('/assignment6/survey/view-results')

@app.route('/assignment6/survey/view-results')
def view_results():
    return send_from_directory(app.static_folder + '/Survey/html', 'results.html')

@app.route('/assignment6/survey/results', methods=['GET'])
def results():
    import json
    db = firestore.client(app=firebase_admin.get_app('survey'))

    fighter = db.collection('votes').document('fighter').get().to_dict()['votes']
    wizard = db.collection('votes').document('wizard').get().to_dict()['votes']
    rogue = db.collection('votes').document('rogue').get().to_dict()['votes']
    cleric = db.collection('votes').document('cleric').get().to_dict()['votes']

    return json.dumps({'fighter': fighter, 'wizard': wizard, 'rogue': rogue, 'cleric': cleric})

@app.route('/assignment7/todo')
def todo():
    return send_from_directory(app.static_folder + '/Todo/html', 'index.html')

@app.route('/assignment7/todo/lists', methods=['GET'])
def lists():
    if request.cookies.get('userid') is None:
        return json.dumps({'error': 'No user id found'})

    userid = request.cookies.get('userid')

    db = firestore.client(app=firebase_admin.get_app('todo'))

    lists = db.collection('lists').document(str(userid)).get().to_dict()

    return json.dumps(lists)

@app.route('/assignment7/todo/add', methods=['POST'])
def add_todo():
    import uuid

    if request.cookies.get('userid') is None:
        userid = uuid.uuid4()
    else:
        userid = request.cookies.get('userid')

    db = firestore.client(app=firebase_admin.get_app('todo'))
    # print(userid)
    data = json.loads(request.data)
    task = data['task']
    listName = data['list']
    # print(task, listName)

    if db.collection('lists').document(str(userid)).get().to_dict() is None:
        db.collection('lists').document(str(userid)).set({f'{listName}': {'task': task, 'completed': False}})
    else:
        db.collection('lists').document(str(userid)).update({f'{listName}': firestore.ArrayUnion([{'task': task, 'completed': False}])})
    
    return json.dumps({'error': False, 'userid': str(userid)})

@app.route('/assignment7/todo/<string:list>/<string:task>/<int:taskID>/toggle')
def toggle_todo(list, task, taskID):
    print(list, task, taskID)

    if request.cookies.get('userid') is None:
        return json.dumps({'error': 'No user id found'})

    userid = request.cookies.get('userid')

    db = firestore.client(app=firebase_admin.get_app('todo'))

    if db.collection('lists').document(str(userid)).get().to_dict() is None:
        return json.dumps({'error': 'No lists found'})
    
    userRef = db.collection('lists').document(str(userid)).get().to_dict()

    try:
        completed = userRef[list][taskID]['completed']
    except:
        completed = userRef[list]['completed']

    db.collection('lists').document(str(userid)).update({f'{list}': firestore.ArrayRemove([{'task': task, 'completed': completed}])})
    db.collection('lists').document(str(userid)).update({f'{list}': firestore.ArrayUnion([{'task': task, 'completed': not completed}])})

    return json.dumps({'success': True})

@app.route('/assignment7/todo/<string:list>/<string:task>/<int:taskID>/delete')
def delete_task(list, task, taskID):
    print(list, task, taskID)

    if request.cookies.get('userid') is None:
        return json.dumps({'error': 'No user id found'})

    userid = request.cookies.get('userid')

    db = firestore.client(app=firebase_admin.get_app('todo'))

    if db.collection('lists').document(str(userid)).get().to_dict() is None:
        return json.dumps({'error': 'No lists found'})
    
    userRef = db.collection('lists').document(str(userid)).get().to_dict()

    try:
        completed = userRef[list][taskID]['completed']
    except:
        completed = userRef[list]['completed']

    db.collection('lists').document(str(userid)).update({f'{list}': firestore.ArrayRemove([{'task': task, 'completed': completed}])})

    return json.dumps({'success': True})

@app.route('/assignment8/quicknotes')
def quicknotes():
    return render_template('login/base.html', session=session)

@app.route('/assignment8/login')
def login():
    authorization_url, state = flow.authorization_url()
    print(state)
    session['state'] = state
    return redirect(authorization_url)

@app.route('/assignment8/logout')
def logout():
    session.clear()
    return redirect('/assignment8/quicknotes')

@app.route('/assignment8/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session['state'] == request.args['state']:
        abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=clientID
    )
    print(id_info)

    session.update(id_info)

    db = firestore.client(app=firebase_admin.get_app('quicknotes'))

    if db.collection('notes').document(session['sub']).get().to_dict() is None:
        db.collection('notes').document(session['sub']).set({})

    return redirect('/assignment8/quicknotes')

@app.route('/assignment8/getNotes')
@loginRequired
def getNotes():
    db = firestore.client(app=firebase_admin.get_app('quicknotes'))

    notes = db.collection('notes').document(session['sub']).get().to_dict()

    return json.dumps(notes)

@app.route('/assignment8/addNote', methods=['POST'])
@loginRequired
def addNote():
    db = firestore.client(app=firebase_admin.get_app('quicknotes'))
    print(request.data)

    data = json.loads(request.data)

    db.collection('notes').document(session['sub']).update({f'{data["title"]}': data['content']})

    return json.dumps({'success': True})

@app.route('/assignment8/deleteNote', methods=['POST'])
@loginRequired
def deleteNote():
    db = firestore.client(app=firebase_admin.get_app('quicknotes'))

    data = json.loads(request.data)

    db.collection('notes').document(session['sub']).update({f'{data["title"]}': firestore.DELETE_FIELD})

    return json.dumps({'success': True})

if __name__ == '__main__':
    print('Running app...')
    app.run()