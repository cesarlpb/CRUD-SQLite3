#%%
import sqlite3 as sql

# Read from db functions
def read_from_db(db_name : str, db_table : str, cols : list, id : int):
    # si no recibe id, entonces devuelve todos los registros
    # si recibe id, entonces devuelve el registro con ese id
    try:
        con = sql.connect(db_name)
        c =  con.cursor()
        
        if cols == []:
            db_cols = '*'
        elif len(cols) <= 3:
            valid_cols = ['id', 'question', 'answer']
            for col in cols:
                if col.lower() not in valid_cols:
                    raise con.Error(f'{col} no es una columna válida')
            db_cols = ', '.join(cols)
        
        if id < 1:
            c.execute(f"SELECT {db_cols} FROM {db_table}")
            questions = c.fetchall()
            return questions
        else:
            c.execute(f"SELECT {db_cols} FROM {db_table} WHERE id = {id}")
            question = c.fetchone()
            return question
    except con.Error as err: # if error
        return err
    finally:
        # pasar a una función aparte <---------------
        # data = c.execute(f"SELECT * FROM {db_table}")
        # cols = []
        # for column in data.description:
        #     cols.append(column[0])
        # print(cols)
        con.close()

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
    # Id es requerido
    try:
        con = sql.connect(db_name)
        c =  con.cursor()
        c.execute(f"DELETE FROM {db_table} WHERE id = {id}")
        con.commit()
        return True
    except con.Error as err:
        return err
    finally:
        con.close()
# %%
