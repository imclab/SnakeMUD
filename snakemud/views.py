from pyramid.view import view_config

@view_config(route_name='home', renderer='snakemud:templates/index.mako')
def index(request):
    return {}
