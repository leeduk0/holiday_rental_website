from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/gallery')
def show_gallery():
    return render_template('gallery.html')


@app.route('/facilities')
def show_facilities():
    return render_template('facilities.html')


@app.route('/reviews')
def show_reviews():
    return render_template('reviews.html')

if __name__ == '__main__':
    app.run(debug=True)
