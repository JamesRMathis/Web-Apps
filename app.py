from flask import Flask, send_from_directory, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(app.static_folder + '/home/html', 'index.html')

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

if __name__ == '__main__':
    print('Running app...')
    app.run()