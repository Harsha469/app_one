print('from views file')

from new_app import app

@app.route('/home')
def home_view():
    return 'hello good morning!!'

