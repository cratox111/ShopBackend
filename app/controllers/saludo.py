from flask import jsonify

def saludo():
    return jsonify({'message':'Hola mundo'})