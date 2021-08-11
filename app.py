from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'bluedtech' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lgcvxgbj:43ujLIsvMZ4vHhiT1zW9RwLuvwYFrgFP@motty.db.elephantsql.com/lgcvxgbj'
db = SQLAlchemy(app)

class Planetas(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagem = db.Column(db.String(500), nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    temperatura = db.Column(db.String(200), nullable=False)
    gravidade = db.Column(db.String(200), nullable=False)
    demais_informacoes = db.Column(db.String(600), nullable=False)
 
    def __init__(self,  imagem, nome, temperatura, gravidade, demais_informacoes):
        self.imagem = imagem
        self.nome = nome
        self.temperatura = temperatura
        self.gravidade = gravidade
        self.demais_informacoes = demais_informacoes

@app.route('/')
def index():
   # session['usuario_logado'] = None
   projetos = Planetas.query.all() 
   return render_template('index.html', projetos=projetos) 

@app.route('/adm')
def adm():
   projetos = Planetas.query.all() 
   return render_template('adm.html', projetos=projetos) 


@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST':
      projeto = Planetas(        
         request.form['imagem'],
         request.form['nome'], 
         request.form['temperatura'],
         request.form['gravidade'],
         request.form['demais_informacoes']
      )
      db.session.add(projeto)
      db.session.commit()
      flash('Projeto Criado!!! ')
      return redirect('/adm')

@app.route('/delete/<id>')
def delete(id):
   projeto = Planetas.query.get(id)
   db.session.delete(projeto)
   db.session.commit()
   return redirect('/adm')

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
   projetoEdit = Planetas.query.get(id)
   if request.method == 'POST':
      projetoEdit.imagem = request.form['imagem']
      projetoEdit.nome = request.form['nome']
      projetoEdit.temperatura = request.form['temperatura']
      projetoEdit.gravidade = request.form['gravidade']
      projetoEdit.demais_informacoes = request.form['demais_informacoes']
      db.session.commit()
      return redirect('/adm')

   return render_template('adm.html', projetoEdit=projetoEdit)



if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)