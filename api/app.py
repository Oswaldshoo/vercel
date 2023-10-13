from flask import Flask, render_template

app = Flask(__name__)


def main():
    register()
    about()
    login()
    contact()
    app.run(debug=True)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__":
    main()

