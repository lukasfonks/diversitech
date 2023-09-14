from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CORS é um mecanismo usado para adicionar cabeçalhos HTTP que informam aos navegadores para permitir
# que uma aplicação Web seja executada em uma origem e acesse recursos de outra origem diferente.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Puxa as configurações do arquivo config.py (configura variáveis da URI com banco de dados)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(port=3000,host='localhost',debug=True)

