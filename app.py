from flask import Flask, send_from_directory, redirect, render_template, request

app = Flask(__name__)

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

if __name__ == '__main__':
    print('Running app...')
    app.run()