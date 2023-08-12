from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Arnold Chris',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"


if __name__ == '__main__':
    app.run(debug=True)