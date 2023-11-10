from data_layout.data_logic import obtener_datos

#Capa de Aplicación

def obtener_posts():
    datos = obtener_datos()
    posts = []
    for dato in datos:
        post = {
            'author': {'username': dato['author']},
            'body': dato['body']
        }
        posts.append(post)
    return posts
