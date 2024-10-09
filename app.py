from flask import Flask, request, make_response, redirect, abort, render_template

app = Flask(__name__)

# Página inicial (Home)
@app.route('/')
def index():
    return render_template('index.html')

# Página de Identificação
@app.route('/identificacao')
def identificacao():
    return render_template('identificacao.html')

# Contexto da Requisição
@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    host = request.host
    return render_template('contexto.html', user_agent=user_agent, ip_address=ip_address, host=host)

@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

if __name__ == '__main__':
    app.run(debug=True)
