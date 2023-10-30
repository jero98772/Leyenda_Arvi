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

  @app.route("/bd1a5db05e1420a1d76c47182958a1cd774827b95cead75adca906b201e45d1d")
  def hit0():
    return render_template("hits/hit0.html")
  @app.route("/d9458b2fbc48779ab7d55c4975af13df8d994ae073fa5f391cbd5c21f6d7716c")
  def hit1():
    return render_template("hits/hit1.html")
  @app.route("/f8e0095506b9988416c331f1a44a063089ff5666c860af3ba16b70896b3d1418")
  def hit2():
    return render_template("hits/hit2.html")
  @app.route("/fbbd3295fcc07d79c7861f5e03330406d3d9cec5120ecd4d78eec4f0bcc77c1a")
  def hit3():
    return render_template("hits/hit3.html")
  @app.route("/0fb039dfb0a69acbc5747cf352dc31632d78a3c504b6da6cd539f6d9806c5705")
  def hit4():
    return render_template("hits/hit4.html")
if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0",port=5000)
