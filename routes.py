# routes.py
import sqlite3 as sql # -> quitar import
from app import app
from flask import render_template, request
from utils import *

# connect to qa_database.sq (database will be created, if not exist)
db_name = 'app.db'
db_table = 'test'
con = sql.connect(db_name)
con.execute(f'CREATE TABLE IF NOT EXISTS {db_table} (ID INTEGER PRIMARY KEY AUTOINCREMENT,'
            + 'Question TEXT, Answer TEXT)')
con.close()

# home page
@app.route('/')  # root : main page
def index():
    # read from database using read_from_db function 
    questions = read_from_db(db_name, db_table, [], 0) # SELECT * FROM test;
    if isinstance(questions, sql.OperationalError) or isinstance(questions, sql.Error):
        return render_template('db_error.html', error=questions, title='Error de conexión')
    else:
        return render_template('index.html', questions=questions, title='Inicio') 
    
# Create question
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        # send the form
        return render_template('create.html', title='Crear Pregunta')
    elif request.method == 'POST':
        # read data from the form and save in variable
        question = request.form['question']
        answer = request.form['answer']

        # store in database
        try:
            con = sql.connect(db_name)
            c =  con.cursor() # cursor
            # insert data
            c.execute(f"INSERT INTO {db_table} (question, answer) VALUES (?,?)",
                (question, answer))
            con.commit() # apply changes
            # go to thanks page
            return render_template('create_thanks.html', question=question, title='¡Gracias!')
        except con.Error as err: # if error
            # then display the error in 'database_error.html' page
            return render_template('db_error.html', error=err, title='Error de conexión')
        finally:
            con.close() # close the connection
    else:
        return 'Método no permitido', 405 # 400 de Bad Request o 405 de método no permitido

# Display all questions in db
@app.route('/questions', methods=['GET'])
def questions():
    # read from database with read_from_db function
    questions = read_from_db(db_name, db_table, ["Id", "Question"], 0) # SELECT Id, Question FROM test;
    if isinstance(questions, sql.OperationalError) or isinstance(questions, sql.Error):
        return render_template('db_error.html', error=questions, title='Error de conexión')
    else:
        return render_template('questions.html', questions=questions, title='Todas las Preguntas')

# Display question
@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
    if request.method == 'GET':
        # read from database with read_from_db function
        questions = read_from_db(db_name, db_table, ["Question"], id) # SELECT * FROM test WHERE id = id;
        if isinstance(questions, sql.OperationalError) or isinstance(questions, sql.Error):
            return render_template('db_error.html', error=questions, title='Error de conexión')
        else:
            return render_template('question.html', question=questions[0], title='Pregunta')
    elif request.method == 'POST':
        submitted_answer = request.form['answer'] # answer from form submitted by user
        # read from database with read_from_db function    
        correct_answer = read_from_db(db_name, db_table, ["Answer"], id) # SELECT Answer FROM test WHERE id = {id};
        if isinstance(correct_answer, sql.OperationalError) or isinstance(correct_answer, sql.Error):
            return render_template('db_error.html', error=correct_answer, title='Error de conexión')
        elif submitted_answer == correct_answer[0]:
            return render_template('correct.html', id=id, title='¡Correcto!')
        else:
            return render_template('sorry.html',
                answer = correct_answer[0],
                yourAnswer = submitted_answer, 
                title="Vuelve a intentarlo :("
            )

# Edit question
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    # if request.form['question'] != None or request.form['question'] != "":
    # update test set question = question, answer = answer where id = id
    # html -> id
    if request.method == 'GET':
        # read from database with read_from_db function    
        question = read_from_db(db_name, db_table, ["Question", "Answer"], id) # SELECT * FROM test WHERE id = id;
        if isinstance(question, sql.OperationalError) or isinstance(question, sql.Error):
            return render_template('db_error.html', error=question, title='Error de conexión')    
        else:
            question, answer = question
            return render_template('edit.html', id=id, question=question, answer=answer, title=f"Editar Pregunta #{id}")
    elif request.method == 'POST':
        # id MUST NOT be changed
            # We store values from form
        new_question = request.form['question']
        new_answer = request.form['answer']
        data = read_from_db(db_name, db_table, ["Question", "Answer"], id) # SELECT Question, Answer FROM test WHERE id = id;
        if isinstance(data, sql.OperationalError) or isinstance(data, sql.Error):
            return render_template('db_error.html', error=data, title='Error de conexión')
        else:
            question, answer = data
            # We validate NOT to have empty fields for update
            if new_question != None or new_question != "":
                question = new_question
            if new_answer != None or new_answer != "":
                answer = new_answer
            # Finally, we update the database
        try:
            con = sql.connect(db_name)
            c =  con.cursor() # cursor
            c.execute(f"UPDATE {db_table} SET Question='{question}', Answer='{answer}' WHERE id = {id}")
            con.commit() # apply changes
            # Reading data to display in thanks page
            question, answer = read_from_db(db_name, db_table, ["Question", "Answer"], id) # SELECT Question, Answer FROM test WHERE id = id;
            # go to thanks page
            return render_template('edit_thanks.html', id=id, question=question, answer=answer, title='¡Editado!')
        except con.Error as err: # if error
            # then display the error in 'database_error.html' page
            return render_template('db_error.html', error=err, title='Error de conexión')
        finally:
            con.close() # close the connection
# Delete question
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    # html thanks page -> id
        # "Se ha borrado la pregunta con id: id" 
    response = delete_from_db(db_name, db_table, id)
    if response == True:
        return render_template('delete_thanks.html', id = id, title='¡Borrado!')
    else:
        return render_template('db_error.html', error=response, title='Error de conexión')