from database import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
  __tablename__ = "usuario"
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(100))
  sus = db.Column(db.String(100))
  email =  db.Column(db.String(100))
  senha = db.Column(db.String(100))
  admin = db.Column(db.Boolean)

  def __init__(self, nome, email, sus, senha, admin):
    self.nome= nome
    self.email= email
    self.sus = sus
    self.senha = senha
    self.admin = admin

  def __repr__(self):
    return '<Usuário{}>'.format(self.nome, self.id)

class Enfermeiro(db.Model, UserMixin):
  __tablename__ = "enfermeiro"
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(100))
  Nregistro = db.Column(db.String(100))
  email =  db.Column(db.String(100))
  senha = db.Column(db.String(100))
  admin = db.Column(db.Boolean)

  def __init__(self, nome, Nregistro, email, senha, admin):
    self.nome = nome
    self.Nregistro = Nregistro
    self.email = email
    self.senha = senha
    self.admin = admin
  
  def __repr__(self):
    return '<Enfermeiro{}>'.format(self.nome, self.id)

class Estoque(db.Model):
  __tablename__ = "estoque"
  id = db.Column(db.Integer, primary_key = True)
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
  id_enfermeiro = db.Column(db.Integer, db.ForeignKey('enfermeiro.id'))
  nome = db.Column(db.String(100))
  observacao = db.Column(db.String(1000))
  tempo_dose = db.Column(db.String(100))
  data_vencimento = db.Column(db.String(100))
  local_vacina = db.Column(db.String(100))
  disponivel = db.Column(db.String(100))
  
  
  def __init__(self, nome, tempo_dose, observacao, data_vencimento, local_vacina, disponivel):
    self.nome = nome
    self.tempo_dose = tempo_dose
    self.observacao = observacao
    self.data_vencimento = data_vencimento
    self.local_vacina = local_vacina
    self.disponivel = disponivel

  def __repr__(self):
    return '<Estoque{}>'.format(self.nome, self.tempo_dose)

class Vacinacao(db.Model):
  __tablename__ = "vacinacao"
  id = db.Column(db.Integer, primary_key = True)
  id_enfermeiro = db.Column(db.Integer, db.ForeignKey('enfermeiro.id'))
  id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
  id_estoque = db.Column(db.Integer, db.ForeignKey('estoque.id'))
  data = db.Column(db.String(100))
  
  def __init__(self, id_enfermeiro, id_usuario, id_estoque, data):
    self.id_usuario = id_usuario
    self.id_enfermeiro = id_enfermeiro
    self.id_estoque = id_estoque
    self.data = data

  def __repr__(self):
    return '<Vacinacao{}>'.format(self.data) 

class Local(db.Model):
  __tablename__="local"
  id = db.Column(db.Integer, primary_key = True)
  nome_local = db.Column(db.String(100))
  endereco = db.Column(db.String(100))

  def __init__(self, nome_local, endereco):
    self.nome_local = nome_local
    self.endereco = endereco

  def __repr__(self):
    return'<Local de Vacinacao{}>'.format(self.nome_local, self.endereco)
  