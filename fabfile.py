import time
import os
import sys

sys.path.insert(0,os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]))

from fabric.api import local, settings, abort, run, env, sudo, put
from fabric.contrib import django
from fabric.contrib.console import confirm
from fabric.contrib.files import exists, get
from fabric.colors import red, green
from fabric.context_managers import prefix, cd

env.project_name = 'pando'
env.hosts = ['192.241.208.161']
env.port = 22
env.virtualenv_name = 'pando'
env.user = 'root'
env.repository_name = 'pando'
env.password = 'database24'
env.repository_url = 'git@github.com:TitoAgudelo/titoarturo.io.git'
env.date = time.strftime('%Y%m%d%H%M%S')

os.environ['DJANGO_SETTINGS_MODULE'] = '%(project_name)s.settings' % env
from django.conf import settings

env.db_name = settings.DATABASES['default']['NAME']
env.db_user = settings.DATABASES['default']['USER']
env.db_password = settings.DATABASES['default']['PASSWORD']
env.db_host = settings.DATABASES['default']['HOST']
env.db_port = settings.DATABASES['default']['PORT']


def active_virtualenvwrapper(func):
    def decorator(*args, **kwargs):
        with prefix('source /home/admin/Workspace/pando/bin/activate'):
            return func(*args, **kwargs)
    return decorator

@active_virtualenvwrapper
def active_environment(func):
    def decorator(*args, **kwargs):
        with prefix('cd /home/admin/Workspace/pando/'):
            return func(*args, **kwargs)
    return decorator

@active_virtualenvwrapper
@active_environment
def virtualenvwrapper(func):
    def decorator(*args, **kwargs):
        with prefix('cd %(repository_name)s' % env):
            return func(*args, **kwargs)
    return decorator

def dependencies():
    print green('Freezing pip requirements')
    local('pip freeze > requirements.txt')


@active_virtualenvwrapper
def remote_make_virtualenv():
    run('mkvirtualenv --no-site-packages %(project_name)s' % env)

@active_virtualenvwrapper
@active_environment
@virtualenvwrapper
def remote_dependencies():
    run('pip install -r requirements.txt')


@active_virtualenvwrapper
@active_environment
@virtualenvwrapper
def update_remote_repository():
    run('git pull')

@active_virtualenvwrapper
@active_environment
@virtualenvwrapper
def sync_database():
    run('./manage.py syncdb')
    run('./manage.py migrate')

@active_virtualenvwrapper
@active_environment
@virtualenvwrapper
def install_requirements():
    run('pip install -r requirements.txt')

def restart():
    try:
        run('supervisorctl stop pando')
        run('supervisorctl start pando')
    except:
        pass

def deploy():
    update_remote_repository()
    install_requirements()
    # sync_database()
    generate_static_dirs()
    try:
        print green('Deployed!')
    except:
        pass

@active_virtualenvwrapper
@active_environment
@virtualenvwrapper
def remote_manage(command):
    run('./manage.py %s' % command)
    
@active_virtualenvwrapper
@active_environment
@virtualenvwrapper
def generate_static_dirs():
    run('./manage.py collectstatic --noinput -v 0')
    
def runserver(port='8000', ip='0.0.0.0'):
    local('./manage.py runserver %s:%s --settings=%s.local_settings'% (ip,port, env.project_name))

def shell():
    local('./manage.py shell --settings=%s.local_settings'% env.project_name)

def validate():
    local('python -m tabnanny **/*.py')

def syncdb():
    local('./manage.py syncdb --settings=%s.local_settings' % env.project_name)
    
def migrate():
    local('./manage.py migrate --settings=%s.local_settings' % env.project_name)