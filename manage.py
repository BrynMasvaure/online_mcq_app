import os
from webapp import create_app, db, migrate
from webapp.models import maths, science

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, maths=maths,science=science, migrate=migrate)