from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, send_from_directory, safe_join, abort
from .model import rus, rusltab, db

words = Blueprint('words', __name__)

@words.route('/')
def home():
    return "Hello World!!"

@words.route('/getRusDictionary')
def getRusDictionary():
    #wordsl = rus.query.all()
    #return jsonify (words = [i.serialize for i in wordsl])
    try:
        return send_from_directory("./static", filename="rus.txt", as_attachment = True)
    except FileNotFoundError:
        return "NOT FOUND FILE"

@words.route('/getRusLatterStatistic')
def getRusLatterStatistic():
    letters = rusltab.query.all()
    return jsonify (letters = [i.serialize for i in letters])
