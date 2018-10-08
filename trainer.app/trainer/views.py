from flask import render_template

from trainer import app

@app.route('/')
def index():
    return render_template('trainer.html')

if __name__ == '__main__':
    app.run()
