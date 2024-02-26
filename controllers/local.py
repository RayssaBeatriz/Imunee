from flask import Blueprint, url_for
from flask import render_template, request, redirect,  flash
from models import Local
from database import db

bp_local = Blueprint("local", __name__, template_folder="templates")

@bp_local.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('localCa.html')

  else:
    nome_local = request.form.get('nome_local')
    endereco = request.form.get('endereco')
    l = Local(nome_local, endereco)
    db.session.add(l) 
    db.session.commit()
    return redirect('/locais')

@bp_local.route('/recovery')
def recovery():
  local = Local.query.all()
  return render_template('local_recovery.html', local=local)

@bp_local.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id): 
  if request.method == 'GET':
    local = Local.query.get(id)
    return render_template('local_delete.html', local = local)

  if request.method == 'POST':
    local = Local.query.get(id)
    db.session.delete(local)
    db.session.commit()
    return redirect('/locais')


@bp_local.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
  if request.method == 'GET':
    local = Local.query.get(id)
    return render_template('local_update.html', local = local)
    
    if request.method=='POST':
      local = Local.query.get(id)
      "local.nome_local = request.form.get('nome')"
      
  else:
    if request.method== 'GET':
      local = Local.query.get(id)
      return render_template('local_update.html', local = local)
      
    if request.method=='POST':
      local = Local.query.get(id)
      local.nome_local = request.form.get('nome_local')
      local.endereco = request.form.get('endereco')

  db.session.add(local) 
  db.session.commit()
  flash('Dados atualizados com sucesso!')
  return redirect('/locais')
