from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Bienvenue dans votre application de gestion immobilière!"