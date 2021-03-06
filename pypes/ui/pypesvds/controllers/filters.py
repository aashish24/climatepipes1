import logging
import json
from pylons import request, response, session, tmpl_context as c
from pylons import app_globals
from pylons.controllers.util import abort

from pypesvds.lib.base import BaseController, render

log = logging.getLogger(__name__)

class FiltersController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('filter', 'filters')

    def index(self, format='html'):
        """GET /filters: All items in the collection"""
        # url('filters')
        type = request.params.getall('node')[0]
        if type == 'Sources':
            s = app_globals.dfg.InputAdapters
        elif type == 'Modules':
            s = app_globals.dfg.Transformers
        elif type == 'Filters':
            s = app_globals.dfg.Filters
        elif type == 'Operators':
            s = app_globals.dfg.Operators
        elif type == 'Extractors':
            s = app_globals.dfg.Extractors
        elif type == 'Visualizations':
            s = app_globals.dfg.OutputAdapters
        else:
            s = '[]'
        return json.dumps(s)

    def create(self):
        """POST /filters: Create a new item"""
        # url('filters')
        klass_name = request.params.getall('klass')[0]
        key = app_globals.dfg.newInstance(klass_name)
        ins = app_globals.dfg.Inputs(key)
        outs = app_globals.dfg.Outputs(key)
        indescs = app_globals.dfg.InputDescs(key)
        outdescs = app_globals.dfg.OutputDescs(key)
        pkg = app_globals.dfg.Package(key)
        ver = app_globals.dfg.Version(key)
        nsp = app_globals.dfg.Namespace(key)
        cache = app_globals.dfg.Cache(key)
        params = app_globals.dfg.Parameters(key)
        return json.dumps([key, ins, outs, pkg, indescs, outdescs, ver, nsp, cache, params])

    def new(self, format='html'):
        """GET /filters/new: Form to create a new item"""
        # url('new_filter')
        pass

    def update(self, id):
        """PUT /filters/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('filter', id=ID),
        #           method='put')
        # url('filter', id=ID)
        for key, value in request.params.iteritems():
            if key != '_method':
                app_globals.dfg.setParam(id, key.encode('utf-8'), value.encode('utf-8'))
        return json.dumps(app_globals.dfg.getComponentConfig(id))

    def delete(self, id):
        """DELETE /filters/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('filter', id=ID),
        #           method='delete')
        # url('filter', id=ID)
        app_globals.dfg.removeInstance(id)

    def show(self, id, format='html'):
        """GET /filters/id: Show a specific item"""
        # url('filter', id=ID)
        return json.dumps(app_globals.dfg.getComponentConfig(id))

    def edit(self, id, format='html'):
        """GET /filters/id/edit: Form to edit an existing item"""
        # url('edit_filter', id=ID)
        pass
