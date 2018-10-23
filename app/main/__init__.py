#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22/022 18:58
# @Author  : K_oul
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes