# run.py

from app import create_app

app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

print("Hola", app)
if app is not None:
    print('Conexión a la base de datos establecida correctamente.')
    app.run(debug=True)
else:
    print('No se pudo establecer la conexión a la base de datos. Revisa los errores anteriores.')