from fabric.api import env, roles, run, local

NETID = None

# Define sets of servers as roles
env.roledefs = {
    'acm': ['ng.acm.uiuc.edu'],
}

# Set the user to use for ssh
env.user = raw_input('Please enter your netid: ')

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
    local('cd %(path)s; git checkout master' % {'path' : local_path})
    build(env='prod')
    local('cd %(path)s; git push origin master' % {'path' : local_path})

    run('cd %(path)s; git checkout master' % {'path' : remote_path})
    run('cd %(path)s; git pull' % {'path' : remote_path})
