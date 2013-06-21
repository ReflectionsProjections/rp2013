from fabric.api import env, roles, run, local, put

# Define sets of servers as roles
env.roledefs = {
    'acm': ['ng.acm.uiuc.edu'],
}


local_path = '~/code/reflections-projections/'
remote_path = '/afs/acm.uiuc.edu/project/rp/www/0000'

def build(env='dev'):
    config = None
    if env == 'prod':
        config = '-c _config_prod.yml'
    elif env == 'stage':
        config = '-c _config_stage.yml'
    local('cd %(path)s; jekyll build %(config)s' % {'path': local_path, 'config': config})

# Restrict the function to the 'web' role
@roles('acm')
def deploy(environment='prod', netid=None):
    # Set the user to use for ssh
    if not netid:
        netid = raw_input('Please enter your netid: ')
    env.user = netid

    build(environment)
    put(local_path + '_site/*', remote_path)
