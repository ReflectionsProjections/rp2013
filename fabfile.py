from fabric.api import env, roles, run, local, put

# Define sets of servers as roles
env.roledefs = {
    'acm': ['ng.acm.uiuc.edu'],
}

envs = {
    "dev": {
        "remote_path": None,
        "config": "_config.yml"
    },
    "stage": {
        "remote_path":  '/afs/acm.uiuc.edu/project/rp/www/0000',
        "config": "_config_stage.yml"
    },
    "prod": {
        "remote_path":  '/afs/acm.uiuc.edu/project/rp/www/2013',
        "config": "_config_prod.yml"
    }
}


local_path = '.' # Project directory.  Change this to absolute to run it from elsewhere

def build(environment='dev'):
    config = envs[environment]['config']
    local('cd %(path)s; jekyll build -c %(config)s' % {'path': local_path, 'config': config })

# Restrict the function to the 'web' role
@roles('acm')
def deploy(environment='prod', netid=None):
    if environment == 'dev':
        raise "Can't deploy while in dev environment! Try prod or stage."
    # Set the user to use for ssh
    if not netid:
        netid = raw_input('Please enter your netid: ')
    env.user = netid
    remote_path = envs[environment]['remote_path']
    build(environment)
    put(local_path + '_site/*', remote_path)
