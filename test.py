#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/19/019 17:09
# @Author  : K_oul
# @File    : test.py
# @Software: PyCharm

from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModeCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()