# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:03:06 2019

@author: candidate
"""
"""import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute('''CREATE TABLE todo1
#             (id integer primary key autoincrement,todo text)''')

conn.commit()
conn.close()"""



from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
    
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text1']
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO todo1 VALUES (null, "tests")')
    #conn.commit()
    print(text)
    conn.close()
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()





#a=my_form_post()
#print(a)    

