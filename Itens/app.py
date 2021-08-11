from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dqpcwtmd:U4RCgVhJ1wqfmTuNbeiA7EtXLxY9daIy@kesavan.db.elephantsql.com/dqpcwtmd'
db = SQLAlchemy(app) 


class Item(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    imagem = db.Column(db.String(500), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    
   
    def __init__(self, nome, imagem, descricao):
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao
        


@app.route('/')
def cadastroItem():
   itens = Item.query.all()
   return render_template('cadastroItem.html', itens=itens) 


@app.route('/new', methods=['GET','POST'])
def new():
   if request.method == 'POST':
      item = Item(
         request.form['nome'],
         request.form['imagem'],
         request.form['descricao']
        
      )
      db.session.add(item)
      db.session.commit()
      flash('Item criado!')
      return redirect('/teste')


if __name__ == '__main__':
   db.create_all() 
   app.run(debug=True)