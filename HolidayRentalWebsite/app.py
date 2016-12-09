from flask import Flask, render_template
from flask import redirect
from flask import request
from flask import url_for

from forms import CommentForm, BookingForm

import csv
from datetime import date
import os

app = Flask(__name__)
app.secret_key = 'SuperSecretKey'

comments_file_path = os.path.abspath('comments.csv')
bookings_file_path = os.path.abspath('bookings.csv')

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
def show_reviews(form=None):
    if form is None:
        form = CommentForm()	
    comments = read_csv_file(comments_file_path)
    return render_template('reviews.html', form=form, comments=comments)


@app.route('/reviews/add', methods=['POST'])
def add_review():
    form = CommentForm()
    if form.validate_on_submit():
        current_date = date.today().strftime('%d/%m/%Y')
        name = request.form['name']
        comment = request.form['comment']
        write_csv_file(comments_file_path, [name, comment, current_date])
        return redirect(url_for('show_reviews'))
    return show_reviews(form)


@app.route('/contact')
def show_contact():
    return render_template('contact.html')


@app.route('/bookings')
def show_bookings(form=None):
    if form is None:
        form = BookingForm()
    bookings = read_csv_file(bookings_file_path)
    return render_template('bookings.html', form=form, bookings=bookings)


@app.route('/bookings/add', methods=['POST'])
def add_booking():
    form = BookingForm()
    if form.validate_on_submit():
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        name = request.form['name']
        email = request.form['email']
        write_csv_file(bookings_file_path, [start_date, end_date, name, email])
        return redirect(url_for('show_bookings'))
    return show_bookings(form)


def read_csv_file(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        file_list = [row for row in reader]
        return file_list


def write_csv_file(file, file_list):
    with open(file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(file_list)
    return

if __name__ == '__main__':
    app.run(debug=True)
