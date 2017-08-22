from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


def read_csv():
    stories = []
    with open("stories.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            stories.append(row)
    return stories


def write_csv(stories):
    with open("stories.csv") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lst)


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


if __name__ == "__main__":
  app.secret_key = 'titkoskulcs'
  app.run(
      debug=True,  # Allow verbose error reports
      port=5000  # Set custom port
  )