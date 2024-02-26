from flask import Blueprint, url_for
from flask import render_template, request, redirect
from models import Vacinacao, Usuario, Estoque
from database import db
from flask_sqlalchemy import SQLAlchemy

bp_vacinacao = Blueprint("vacinacao", __name__, template_folder="templates")

@bp_vacinacao.route('/create')
def create():
    suss = str("123")
    id_usuario = Usuario.query.filter_by(sus = suss).first().id
    estoque = str("variola")
    id_estoque = Estoque.query.filter_by(id = estoque)
    return str(id_usuario)
    estoque = str("variola")
  
'''
@bp_local.route('/recovery')
def recovery():
  local = Local.query.all()
  return render_template('local.html', local=local)

@bp_local.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id): 
  if request.method == 'GET':
    local = Local.query.get(id)
    return render_template('local_delete.html', local = local)

  if request.method == 'POST':
    local = Local.query.get(id)
    db.session.delete(local)
    db.session.commit()
    return redirect(url_for('.recovery'))

"""""
@bp_local.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
  if request.method == 'GET':
    local = Local.query.get(id)
    return render_template('estoque_update.html', estoque = estoque)
    if request.method=='POST':
      estoque = estoque.query.get(id)
      estoque.email = request.form.get('email')
  else:
    if request.method== 'GET':
      usuario= Estoque.query.get(id)
      return render_template('admin_update.html', usuario=usuario)
    if request.method=='POST':
      usuario = Estoque.query.get(id)
      usuario.nome = request.form.get('nome')
      usuario.email = request.form.get('email')

  db.session.add(usuario) 
  db.session.commit()
  flash('Dados atualizados com sucesso!')
  return redirect(url_for('.recovery'))
'''