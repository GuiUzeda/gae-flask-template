from flask import Flask, render_template

app = Flask(__name__)

app.config.update(
    DEBUG=False,
)

@app.route('/')
def show_main():

    return render_template('index.html')

if __name__ == '__main__':
    app.config.update(
    DEBUG=True,
)

    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
