# -*- coding: utf-8 -*-

import codecs
import json
import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

class Archive(object):
    def Loader(self, dir):


@app.route('/')
def index():
    return redirect(url_for('aboutme'))

@app.route('/aboutme')
def aboutme():
    aboutme = json.loads(codecs.open('data/aboutme.json', 'r', encoding='utf-8').read())
    return render_template('aboutme.html', aboutme=aboutme)

@app.route('/tags')
def tags():
    tags = json.loads(codecs.open('data/tags.json', 'r', encoding='utf-8').read())
    return render_template('tags.html', tags=tags)

@app.route('/tagsdetail/<tag>')
def tag_detail(tag):
    return "Wating..."

@app.route('/archives')
def archives():
    return "Wating..."

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


