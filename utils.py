# Read from db functions
def read_from_db(db_name, db_table, cols, id):
    # si no recibe id, entonces devuelve todos los registros
    # si recibe id, entonces devuelve el registro con ese id
    pass
    # try:
    #     con = sql.connect(db_name)
    #     c =  con.cursor()
    #     c.execute(f"SELECT * FROM {db_table} WHERE id = {id}")
    #     id, question, answer = c.fetchone() # current values for id, question, answer
    #     con.commit()
    #     return id, question, answer
    # except con.Error as err: # if error
    #     # then display the error in 'database_error.html' page
    #     return render_template('db_error.html', error=err, title='Error de conexión')
    # finally:
    #     con.close()

# Write to db functions
def write_to_db(db_name, db_table, cols, values):
    # INSERT no necesita id porque es autoincremental
    pass
    # try:
    #     con = sql.connect(db_name)
    #     c =  con.cursor() # cursor
    #     c.execute(f"INSERT INTO {db_table} ({cols}) VALUES ({values})")
    #     con.commit() # apply changes
    #     return True
    # except con.Error as err: # if error
    #     # then display the error in 'database_error.html' page
    #     return render_template('db_error.html', error=err, title='Error de conexión')
    # finally:
    #     con.close() # close the connection
# Update db functions
def update_db(db_name, db_table, cols, values, id):
    # id es requerido
    pass
    # try:
    #     con = sql.connect(db_name)
    #     c =  con.cursor() # cursor
    #     c.execute(f"UPDATE {db_table} SET {cols} WHERE id = {id}")
    #     con.commit() # apply changes
    #     return True
    # except con.Error as err: # if error
    #     # then display the error in 'database_error.html' page
    #     return render_template('db_error.html', error=err, title='Error de conexión')
    # finally:
    #     con.close() # close the connection
# Delete from db functions
def delete_from_db(db_name, db_table, id):
    # id es requerido
    pass
    # try:
    #     con = sql.connect(db_name)
    #     c =  con.cursor() # cursor
    #     c.execute(f"DELETE FROM {db_table} WHERE id = {id}")
    #     con.commit() # apply changes
    #     return True
    # except con.Error as err: # if error
    #     # then display the error in 'database_error.html' page
    #     return render_template('db_error.html', error=err, title='Error de conexión')
    # finally:
    #     con.close() # close the connection