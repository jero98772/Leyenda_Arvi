#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Leyenda_Arvi - by Super_estrellas_mutantes_asesinas
from flask import Flask, render_template, request, flash, redirect ,session
app = Flask(__name__)
class webpage():
  @app.route("/")
  def index():
    return render_template("index.html")
      
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
