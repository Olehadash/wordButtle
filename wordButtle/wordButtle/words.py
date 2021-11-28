from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, send_from_directory, safe_join, abort
from .model import rus, rusltab, db, eng, heb, englab

words = Blueprint('words', __name__)

@words.route('/')
def home():
    return "Hello World!!"

@words.route('/getRusDictionary', methods=['POST'])
def getRusDictionary():
    leng = request.form.get('leng')
    try:
        if leng == "ru":
            return send_from_directory("./static", filename="rus.txt", as_attachment = True)
        elif leng == "en":
            return send_from_directory("./static", filename="eng.txt", as_attachment = True)
        elif leng == "he":
            return send_from_directory("./static", filename="heb.txt", as_attachment = True)
    except FileNotFoundError:
        return "NOT FOUND FILE"

@words.route('/getRusLatterStatistic', methods=['POST'])
def getRusLatterStatistic():
    leng = request.form.get('leng')
    letters = rusltab.query.all()
    if leng == "en":
        letters = englab.query.all()
    elif leng == "he":
        letters = englab.query.all()
    return jsonify (letters = [i.serialize for i in letters])

@words.route('/getDictionary')
def getDictionary():
    wordsl = heb.query.all()
    return jsonify (words = [i.serialize for i in wordsl])
