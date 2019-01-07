from . import app_2

@app_2.route('/')
def index():
    return 'Hello app_2'
