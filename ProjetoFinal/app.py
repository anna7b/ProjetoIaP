from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/modelo')
def modelo():
    return render_template('modelo.html')

@app.route('/cursos')
def cursos():
    cursos = []
    with open('cursos.csv', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        for linha in leitor:
            cursos.append(linha)
    return render_template('cursos.html', cursos=cursos)

@app.route('/novocurso')
def novocurso():
    return render_template('novocurso.html')

@app.route('/novocurso', methods=['POST', ])
def criarcurso():
    curso = request.form['curso']
    descricao = request.form['descricao']
    cargahoraria = request.form['cargahoraria']
    with open('cursos.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow([curso, descricao, cargahoraria])
    return redirect(url_for('cursos'))

@app.route('/excluircurso/<int:curso_id>', methods= ['POST', ])
def excluircurso(curso_id):
    with open('cursos.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
    for i, linha in enumerate(linhas):
        if i == curso_id:
            del linhas[i]
            break
    with open('cursos.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(linhas)
    return redirect(url_for('cursos'))


@app.route('/agenda')
def agenda():
    agenda = []
    with open('agenda.csv', newline='', encoding='utf-8') as arquivo2:
        leitor2 = csv.reader(arquivo2, delimiter=';')
        for linha2 in leitor2:
            agenda.append(linha2)
    return render_template('agenda.html', agenda=agenda)

@app.route('/novoevento')
def novoevento():
    return render_template('novoevento.html')

@app.route('/novoevento', methods=['POST', ])
def criarevento():
    data = request.form['data']
    descricao2 = request.form['descricao2']
    tipo = request.form['tipo']
    with open('agenda.csv', 'a', newline='', encoding='utf-8') as arquivo2:
        escritor2 = csv.writer(arquivo2, delimiter=';')
        escritor2.writerow([data, descricao2, tipo])
    return redirect(url_for('agenda'))

@app.route('/excluirevento/<int:evento_id>', methods= ['POST', ])
def excluirevento(evento_id):
    with open('agenda.csv', 'r', newline='', encoding='utf-8') as arquivo2:
        leitor2 = csv.reader(arquivo2)
        linhas2 = list(leitor2)
    for x, linha2 in enumerate(linhas2):
        if x == evento_id:
            del linhas2[x]
            break
    with open('agenda.csv', 'w', newline='', encoding='utf-8') as arquivo2:
        escritor2 = csv.writer(arquivo2)
        escritor2.writerows(linhas2)
    return redirect(url_for('agenda'))

app.run(debug=True, port=8080)
