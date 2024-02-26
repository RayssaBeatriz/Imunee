from flask import Flask, render_template, request
from flask import Blueprint
from database import db, lm
from flask_migrate import Migrate
from controllers.usuarios import bp_usuarios
from controllers.enfermeiros import bp_enfermeiros
from controllers.estoque import bp_estoque
from controllers.vacinacao import bp_vacinacao
from controllers.local import bp_local
from flask_login import current_user
from models import Usuario 
from models import Enfermeiro
from models import Estoque
from models import Local
from models import Vacinacao

app = Flask(__name__)
app.config['SECRET_KEY'] = 'palavra-secreta'
conexao = "sqlite:///cid.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_enfermeiros, url_prefix='/enfermeiros')
app.register_blueprint(bp_estoque, url_prefix='/estoque')
app.register_blueprint(bp_local, url_prefix='/local')
app.register_blueprint(bp_vacinacao, url_prefix='/vacinacao')


db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)

    
@app.route('/')
def index():
  if current_user.is_authenticated:
    return render_template('dashboard.html', nome=current_user.nome)
  else:
    return render_template('landing.html')

@app.route('/escolhaca')
def escolhaca():
  return render_template('escolha.html')

@app.route('/escolhalo')
def escolhalo():
  return render_template('escolhalo.html')

@app.route('/loginPa')
def loginPa():
  return render_template('loginPa.html')

@app.route('/logine')
def logine():
  return render_template('loginEn.html')

@app.route('/cadastro')
def cadastroPa():
  return render_template('cadastroPa.html')

@app.route('/cadastroEn')
def cadastroEn():
  return render_template('cadastroEn.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/vacinas')
def vacinas():
  estoque = Estoque.query.all()
  return render_template('vacinasPa.html', estoque=estoque)

@app.route('/cavacinas')
def cavacinas():
  return render_template('cadastroVa.html')

@app.route('/locais')
def locais():
  local = Local.query.all()
  return render_template('local.html', local=local)

@app.route('/calocais')
def calocais():
  return render_template('localCa.html')

app.run(host='0.0.0.0', port=81)