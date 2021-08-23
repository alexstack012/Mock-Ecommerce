from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask import jsonify
from flask_app import app


# ======================================================= #
# ==== BASE =========#
# ======================================================= #

@app.route("/")
def enter():
    return render_template('index.html')


# ======================================================= #
# ==== Why Us =========#
# ======================================================= #

@app.route("/why")
def why():
    return render_template('why.html')


# ======================================================= #
# ==== Contact Us =========#
# ======================================================= #


@app.route("/contact")
def contact():
    return render_template('contactUs.html')

# ======================================================= #
# ==== Product view pages =========#
# ======================================================= #


@app.route("/product/1")
def prod1():
    return render_template('product1.html')


@app.route("/product/2")
def prod2():
    return render_template('product2.html')


@app.route("/product/3")
def prod3():
    return render_template('product3.html')

# ======================================================= #
# ==== View Cart =========#
# ======================================================= #


# ======================================================= #
# ==== Checkout =========#
# ======================================================= #
