from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game/<game_name>")
def run_game(game_name):
    game_file = f"games/{game_name}.py"
    if os.path.exists(game_file):
        os.system(f"python {game_file}")
        return f"Game {game_name} selesai dimainkan!"
    return "Game tidak ditemukan!", 404

if __name__ == "__main__":
    app.run(debug=True)
