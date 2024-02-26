from flask import Blueprint, url_for
from flask import render_template, request, redirect, flash
from models import Estoque
from database import db
from datetime import date

bp_estoque = Blueprint("estoque", __name__, template_folder="templates")

@bp_estoque.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('CadastroVa.html')

  else:
    data_vencimento = request.form.get('data_vencimento')
    nome = request.form.get('nome')
    observacao = request.form.get('observacao')
    local_vacina = request.form.get('local_vacina')
    tempo_dose = request.form.get('tempo_dose')
    disponivel = request.form.get('disponivel')
    e = Estoque(nome, tempo_dose, observacao, data_vencimento, local_vacina, disponivel)
    db.session.add(e) 
    db.session.commit()
    return redirect('/vacinas')

@bp_estoque.route('/recovery')
def recovery():
  estoque = Estoque.query.all()
  return render_template('vacinasPa.html', estoque=estoque)

@bp_estoque.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id): 
  if request.method == 'GET':
    estoque = Estoque.query.get(id)
    return render_template('estoque_delete.html', estoque = estoque)

  if request.method == 'POST':
    estoque = Estoque.query.get(id)
    db.session.delete(estoque)
    db.session.commit()
    return redirect(url_for('.recovery'))

@bp_estoque.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
  if request.method== 'GET':
    estoque= Estoque.query.get(id)
    return render_template('estoque_update.html', estoque = estoque)
    if request.method=='POST':
      estoque = estoque.query.get(id)
      estoque.disponivel = int(request.form.get('disponivel'))
  else:
    if request.method== 'GET':
      estoque= Estoque.query.get(id)
      return render_template('admin_update.html', estoque = estoque)
    if request.method=='POST':
      estoque = estoque.query.get(id)
      estoque.disponivel = int(request.form.get('disponivel'))

  db.session.add(estoque) 
  db.session.commit()
  flash('Dados atualizados com sucesso!')
  return redirect(url_for('.recovery'))
