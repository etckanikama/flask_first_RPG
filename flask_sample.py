from flask import Flask, render_template
app = Flask(__name__)

player ="勇者"
@app.route('/')
def menu():
    #players= ["戦士","勇者","魔法使い"]
    #name= "Flask"
    return render_template('menu.html',player=player)

@app.route('/walk')
def walk():
    message = player + "はあるいていた"
    return render_template("action.html",player = player ,message = message)

@app.route('/attack')
def attack():
    message = player + "はモンスターと戦った"
    return render_template("action.html",player = player ,message = message)

if __name__ == '__main__':
    app.run()