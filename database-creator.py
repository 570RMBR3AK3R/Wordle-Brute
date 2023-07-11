############################ CREATION OF DATABASE ########################

import mysql.connector as sq

j = input('Enter your sql password : ')

con = sq.connect(host = 'localhost', user = 'root', password = j)

c1 = con.cursor()
h = 'create database wordle_crack'
c1.execute(h)
con.commit()

c2 = con.cursor()
h2 = 'use wordle_crack'
c2.execute(h2)


########################### CREATING TABLE IN SQL ###################################

c3 = con.cursor()
qry = 'create table word_list(words varchar(7))'
c3.execute(qry)
con.commit()

print('all ok')

