from flask import Flask,render_template,Response,request,jsonify
import requests


app=Flask(__name__)
# To prevent caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# prevent cached responses
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


@app.route('/')
def start():
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)