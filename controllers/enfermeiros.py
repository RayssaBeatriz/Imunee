from flask import render_template, request, redirect, flash
from models import Enfermeiro
from database import db
from flask import Blueprint, url_for
from flask_login import login_user, logout_user, login_required, current_user

bp_enfermeiros = Blueprint("enfermeiros", __name__, template_folder='templates')

@bp_enfermeiros.route('/recovery', methods=['GET', 'POST'])
def recovery():
    enfermeiros = Enfermeiro.query.all()
    return render_template("enfermeiros_recovery.html", enfermeiros = enfermeiros)

@bp_enfermeiros.route('/create', methods= ['GET', 'POST'])
def create():
  if request.method== 'GET':
    return render_template('cadastroEn.html')
  else:
    nome = request.form.get('nome')
    Nregistro = request.form.get('Nregistro')
    email= request.form.get('email')
    senha= request.form.get('senha')
    csenha= request.form.get('senha2')
    admin = 1
    enfermeiro = Enfermeiro(nome, Nregistro, email, senha, admin)
    db.session.add(enfermeiro)
    db.session.commit()

    if senha==csenha:
      flash('Dados registrados com sucesso')
      enfermeiro = Enfermeiro.query.filter_by(email = email).first()
      login_user(enfermeiro)
      return redirect('/')
    elif senha != csenha:
      flash('Senhas não conferem')
      return redirect(url_for('.create'))

@bp_enfermeiros.route('/autenticar', methods=['POST'])
def autenticar():
  email = request.form.get('email')
  senha = request.form.get('senha')
  enfermeiro = Enfermeiro.query.filter_by(email = email).first()
  if enfermeiro and senha == enfermeiro.senha:
    login_user(enfermeiro)
    return redirect('/')
  else:
    flash('Dados incorretos', 'danger')
    return redirect('/login')
