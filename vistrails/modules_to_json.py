import itertools
import json

def create_components(reg, vt_package):
    modules = []
    for desc in vt_package.descriptor_list:
        module = {"name": desc.name,
                  "container": \
                      {"xtype": "climatePipes.Container",
                       "icon": "wireit/res/icons/application_edit.png",
                       "fields": [],
                       "terminals": [],
                       "vt": {"cache": 1,
                              "namespace": desc.namespace,
                              "package": desc.package,
                              "version": desc.package_version},
                       }
                  }
        container = module["container"]
        
        ports = {'input': [], 'output': []}
        ports['input'] = reg.module_destination_ports_from_descriptor(True,
                                                                      desc)
        ports['output'] = reg.module_source_ports_from_descriptor(True, desc)
        # for port_spec in desc.port_specs_list:
        #     ports[port_spec.type].append((port_spec.name, port_spec.sigstring))


        for port_type, port_specs in ports.iteritems():
            num_ports = sum(1 for ps in port_specs if not ps.optional)
            x_offset = 320.0 / (num_ports + 1)
            x_step = 320.0 / (num_ports + 1)
            for port_spec in port_specs:
                is_input = port_type == "input"
                if not port_spec.optional:
                    if is_input:
                        portType = "i" + port_spec.sigstring
                        allowedTypes = ["o" + port_spec.sigstring]
                    else:
                        portType = "o" + port_spec.sigstring
                        allowedTypes = []
                        allDescs = []
                        for ps_desc in port_spec.descriptors():
                            indexDescs = []
                            for d in reg.get_module_hierarchy(ps_desc):
                                indexDescs.append(d)
                            allDescs.append(indexDescs)
                        for descs in itertools.product(*allDescs):
                            aType = "i(" + \
                                ",".join(d.sigstring for d in descs) + ")"
                            allowedTypes.append(aType)
                            
                    terminal = {"name": port_spec.name,
                                "direction": \
                                    [0,-1] if is_input else [0,1],
                                "offsetPosition": {"left": x_offset,
                                                   "top" if is_input \
                                                       else "bottom":\
                                                       -15},
                                "ddConfig": {"type": portType,
                                             "allowedTypes": allowedTypes},
                                }
                    container["terminals"].append(terminal)
                    x_offset += x_step
                if reg.is_method(port_spec):
                    field = {"inputParams": {"label": port_spec.name,
                                             "name": port_spec.name.lower(),
                                             "required": True},
                             "type": "string",
                             "alias": "",
                             "vtype": port_spec.sigstring[1:-1],
                             }
                    container["fields"].append(field)
        modules.append(module)
    modules.sort(key=lambda x: x["name"])
    print "var vt_modules =", json.dumps(modules, indent=1)
                
def run():
    import sys
    sys.path.append('/vistrails/src/git/vistrails')
    import core.application as vt_app
    vt_app.init({'dotVistrails': '/Users/dakoop/.vistrails.cmdline'})

    from core.modules.module_registry import get_module_registry
    reg = get_module_registry()
    basic_pkg = reg.get_package_by_name('edu.utah.sci.vistrails.basic')
    create_components(reg, basic_pkg)

if __name__ == '__main__':
    run()
    
