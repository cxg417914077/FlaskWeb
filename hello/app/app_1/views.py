from . import app_1

@app_1.route('/')
def index():
    return 'Hello app_1!'
