from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime, timedelta
import threading
import time 

app = Flask(__name__)

# Diretórios
MANUAL_HTML_DIR = 'manual_html'
SAVED_HTML_DIR = 'saved_html'
TEMPLATES_DIR = 'templates'

# URL do Confluence
CONFLUENCE_URL = 'https://sapiensia.atlassian.net/wiki/spaces/SIA/pages/648118276/SUM+RIO+DE+FUNCIONALIDADES'

# Função para raspar dados
def scrape_data():
    response = requests.get(CONFLUENCE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()

# Função para salvar HTML
def save_html(directory, content):
    filename = os.path.join(directory, f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.html')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# Rota principal
@app.route('/')
def index():
    files = sorted(os.listdir(SAVED_HTML_DIR), reverse=True)
    if files:
        latest_file = os.path.join(SAVED_HTML_DIR, files[0])
        with open(latest_file, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = "Nenhum dado encontrado."
    return render_template('index.html', content=content)

# Rota para extração manual
@app.route('/manual_extraction')
def manual_extraction():
    content = scrape_data()
    save_html(MANUAL_HTML_DIR, content)
    return render_template('manual_extraction.html', content=content)

# Rota para voltar à página inicial
@app.route('/back')
def back():
    return redirect(url_for('index'))

# Função para extração automática a cada 12 horas
def scheduled_scrape():
    while True:
        content = scrape_data()
        save_html(SAVED_HTML_DIR, content)
        time.sleep(43200)  

# Iniciar o thread de extração automática
threading.Thread(target=scheduled_scrape, daemon=True).start()

if __name__ == '__main__':
    if not os.path.exists(MANUAL_HTML_DIR):
        os.makedirs(MANUAL_HTML_DIR)
    if not os.path.exists(SAVED_HTML_DIR):
        os.makedirs(SAVED_HTML_DIR)
    app.run(debug=True)
