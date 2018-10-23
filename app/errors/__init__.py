#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22/022 18:34
# @Author  : K_oul
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers