import sys
import os

curr_dir = os.getcwd()
vt_home = os.environ(['VISTAILS_HOME'])

sys.path.append(vt_home)

import core.application as vt_app
vt_app.init()

import core.api
from core.log.module_exec import ModuleExec
vt = core.api.get_api()

vt.load_vistrail(curr_dir + "/files/helloworld.vt")
vt.select_version("Merge1")
vt.execute()
wf_execs = vt.get_all_executions()

for wf_exec in wf_execs:
    print wf_exec.ts_start, wf_exec.ts_end, wf_exec.user, wf_exec.vt_version
    for item_exec in wf_exec.item_execs:
        if type(item_exec) == ModuleExec:
            print ' ', item_exec.module_name, item_exec.ts_start, \
                item_exec.ts_end, item_exec.completed

print
print '== FIRST EXECUTION PROVENANCE =='

wf_version = wf_execs[0].parent_version
vt.select_version(wf_version)
wf = vt.get_current_workflow()
for item_exec in wf_execs[0].item_execs:
    if type(item_exec) == ModuleExec:
        module = wf.modules[item_exec.module_id]
        print module.package + ':' + module.name, \
            '(' + module.version + ')', item_exec.ts_start, \
            item_exec.ts_end, item_exec.completed
        for parameter_list in module.functions:
            print ' -', parameter_list.name,
            for parameter in parameter_list.parameters:
                print parameter.type, parameter.strValue
for conn in wf.connection_list:
    print conn.source.moduleName, '(' + str(conn.source.name) + ') ->', \
        conn.destination.moduleName, '(' + str(conn.destination.name) + ')'

vt.close_vistrail()
