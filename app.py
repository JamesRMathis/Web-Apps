from flask import Flask, send_from_directory, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(app.static_folder + '/home/html', 'index.html')

@app

@app.route('/bio')
def bio():
    return send_from_directory(app.static_folder + '/bio-site/html', 'bio.html')

@app.route('/schedule')
def schedule():
    return send_from_directory(app.static_folder + '/bio-site/html', 'schedule.html')

@app.route('/favorites')
def favorites():
    return send_from_directory(app.static_folder + '/bio-site/html', 'favorites.html')

if __name__ == '__main__':
    print('Running app...')
    app.run()