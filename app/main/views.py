# -*- coding: utf-8 -*-

import codecs
import json
import os
from flask import Flask, render_template, redirect, url_for
from . import main

@main.route('/')
def index():
    return redirect(url_for('aboutme'))

@main.route('/aboutme')
def aboutme():
    aboutme = json.loads(codecs.open('/temp_cp/train/myblog_demo_8_12/myblog/app/data/aboutme.json', 'r', encoding='utf-8').read())
    # aboutme = {"姓名": "陈鹏", "什么": "上帝保佑"}
    return render_template('aboutme.html', aboutme=aboutme)
    # print "any is ok."
    # return render_template('base_style.html')

@main.route('/tags')
def tags():
    tags = json.loads(codecs.open('/temp_cp/train/myblog_demo_8_12/myblog/app/data/tags.json', 'r', encoding='utf-8').read())
    return render_template('tags.html', tags=tags)

@main.route('/tagsdetail/<tag>')
def tag_detail(tag):
    return "Wating..."

@main.route('/archives')
def archives():
    return "Wating..."