import os

from flask import Flask

def createApp(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)

    #try:
    #    os.makedirs(app.instance_path)
    #except OSError:
    #    print("Instance path not found")
    try:
        os.makedirs(app.instance_path)
    except FileExistsError:
        print("Directory already exists.")
    except PermissionError:
        print("Insufficient permissions to")

    @app.route('/')
    def welcome():
        return 'Shower Thoughts!'
    
    import db
    import auth
    import blog
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    app.debug = True
    app.run()

if __name__ == "__main__":
    createApp()