from fabric.api import env, roles, run, local, put

NETID = None

# Define sets of servers as roles
env.roledefs = {
    'acm': ['ng.acm.uiuc.edu'],
}

# Set the user to use for ssh
if not NETID:
    NETID = raw_input('Please enter your netid: ')
env.user = NETID

local_path = '~/code/reflections-projections/'
remote_path = '/afs/acm.uiuc.edu/project/rp/www/0000'

def build(env='dev'):
    config = None
    if env == 'prod':
        config = '-c _config_prod.yml'
        local('cd %(path)s; jekyll build %(config)s' % {'path': local_path, 'config': config})

# Restrict the function to the 'web' role
@roles('acm')
def deploy():
    build(env='prod')
    put(local_path + '_site/*', remote_path)
