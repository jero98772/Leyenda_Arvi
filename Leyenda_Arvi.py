#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Leyenda_Arvi - by Super_estrellas_mutantes_asesinas
from flask import Flask, render_template, request, flash, redirect ,session
app = Flask(__name__)
class webpage():
  @app.route("/")
  def index():
    return render_template("index.html")
      
  @app.route("/p1")
  def p1():
    return render_template("maps/1point.html")

  @app.route("/p2")
  def p2():
    return render_template("maps/2point.html")

  @app.route("/p3")
  def p3():
    return render_template("maps/3point.html")

  @app.route("/p4")
  def p4():
    return render_template("maps/4point.html")

  @app.route("/p5")
  def p5():
    return render_template("maps/5point.html")
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
