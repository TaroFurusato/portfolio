from flask_script import Manager 
from portfolio import app 
from portfolio.scripts.db import InitDB

# DBファイルの作成 コマンド: python manage.py init_db
if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())

    manager.run()