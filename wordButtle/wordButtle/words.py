from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from .model import rus, rusltab, db

words = Blueprint('words', __name__)

@words.route('/')
def home():
    return "Hello World!!"

@words.route('/getRusDictionary')
def getRusDictionary():
    wordsl = rus.query.all()
    return jsonify (words = [i.serialize for i in wordsl])

@words.route('/getRusLatterStatistic')
def getRusLatterStatistic():
    letters = rusltab.query.all()
    return jsonify (letters = [i.serialize for i in letters])
