#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17/017 18:15
# @Author  : K_oul
# @File    : errors.py
# @Software: PyCharm

from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500