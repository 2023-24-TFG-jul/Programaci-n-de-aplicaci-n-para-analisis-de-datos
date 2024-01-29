#Nombre: Prototipo
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.001
#Descripción: Por ahora nada
import psycopg2

conn=psycopg2.connect(host="localhost",dbname="postgres", user="postgres", password="1234",port=5432)