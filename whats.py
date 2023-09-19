# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:38:12 2022

@author: LTP-5
"""

from mysql import connector
import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


mydb = connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345')


@app.route('/', methods = ['GET'])


def bot():
    
    query = ('SELECT warranty_expire_date FROM qubeslocal.asset_secondary;')
    incoming_message = request.values.get('Body')
    response = MessagingResponse()
    message = response.message()
    
    for incoming_message in query:
        print(i)
    
    
