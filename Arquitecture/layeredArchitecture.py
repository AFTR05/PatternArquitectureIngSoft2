from flask import Flask, render_template
from application_layout.app_logic import obtener_posts

app = Flask(__name__,template_folder='presentation_layout/templates')

#Capa de presentacion

@app.route('/')
def index():
    posts = obtener_posts()
    return render_template('index.html', title='Home', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
