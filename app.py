from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    return "heloo"

app.route('/msb')
def msb():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
