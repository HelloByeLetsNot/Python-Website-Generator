from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
    content = request.form['content']
    return render_template('website.html', title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)
