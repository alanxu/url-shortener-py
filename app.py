from flask import Flask, render_template, request, redirect

import shortener
import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tinyurl', methods=['POST'])
def shorten():
    url = request.form['url']
    record = db.find_by_url(url)
    if not record:
        _id = shortener.get_id(url)
        token = shortener.get_url_token(_id, url)
        db.save(_id, url, token)
    else:
        token = record['token']

    short_url = f"{request.host_url}{token}"
    return render_template('result.html', short_url=short_url)


@app.route('/<token>')
def redirect_url(token):
    record = db.find_by_token(token)
    return redirect(f'http://{record["url"]}', code=302)


if __name__ == '__main__':
    app.run(debug=True)
