from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


@app.route('/story')
def route_story():
    return render_template('story.html')


@app.route('/')
def route_index():
    return render_template('index.html')


if __name__ == "__main__":
  app.secret_key = 'titkosjelszo'
  app.run(
      debug=True,  # Allow verbose error reports
      port=5000  # Set custom port
  )