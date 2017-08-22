from flask import Flask, render_template, redirect, request, session
import csv
import uuid
import os


app = Flask(__name__)


def generate_id():
    new_id = uuid.uuid4()
    return str(new_id)


def read_csv():
    stories = []
    with open("stories.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            stories.append(row)
    return stories


def write_csv(stories):
    with open("stories.csv","a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(stories)


@app.route('/story')
def route_story():
    return render_template('story.html')


@app.route('/')
def route_index():
    stories = read_csv()
    return render_template('index.html', stories=stories)


@app.route('/story/<int:post_id>')
def route_edit_story(post_id):
    return render_template('story.html')

@app.route('/save_story',methods=["POST"])
def route_save_story():
    list_label = ["storytitles","userstory","acceptance","business","estimation"]
    stories = []
    new_id = generate_id()
    stories.insert(0, new_id)
    for i in list_label:
        stories.append(request.form[i])
    write_csv(stories)
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = 'titkoskulcs'
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
