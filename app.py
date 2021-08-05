
from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message #Importa o Mail e o Message do flask_mail para facilitar o envio de emails
from flask_sqlalchemy import SQLAlchemy # ORM responsável por realizar as operações do banco de dados via Python
# from mail_config import email, mail_senha # Módulo para esconder meu user e senha do email.

app = Flask(__name__)
app.secret_key = 'bluedtech'