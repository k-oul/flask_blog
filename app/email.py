#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20/020 15:51
# @Author  : K_oul
# @File    : email.py
# @Software: PyCharm

from flask_mail import Message
from app import mail, current_app
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(),msg)).start()

