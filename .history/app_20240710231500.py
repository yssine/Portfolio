from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('WhoAmI.html')

@app.route('/WhoAmI')
def WhoAmI():
    return render_template('WhoAmI.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/education')
def education():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug=True)
