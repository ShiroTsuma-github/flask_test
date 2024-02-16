from packages import app
from flask import render_template, request, redirect, url_for
from flask import g


@app.route('/')
def index():
    return 'test'