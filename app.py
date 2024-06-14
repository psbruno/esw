from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Obter todas as tarefas"""
    # Dados fictícios de exemplo
    tasks = [
        {'id': 1, 'title': 'Lorem Ipsum', 'description': 'Lorem ipsum dolor sit amet'},
        {'id': 2, 'title': 'Dolor Sit', 'description': 'Consectetur adipiscing elit'}
    ]
    return jsonify(tasks)

@app.route('/docs', methods=['GET'])
def docs():
    """Servir a documentação da API"""
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
