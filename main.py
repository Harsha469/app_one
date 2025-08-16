print('from mainfile')
from new_app import app
from new_app import views



if __name__ == '__main__':
    app.run(debug = True)