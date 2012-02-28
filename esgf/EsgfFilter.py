import core.modules.module_registry
from core.modules.vistrails_module import Module, ModuleError
import esgf

version = "0.9.0"
name = "EsgfFilter"
identifier = "edu.utah.sci.vistrails.esgffilter"

# ------------------------------------------------------------------------class
class EsgfFilter(Module):
    """EsgfFilter is a module that downloads metadata form ESGF."""

    def compute(self):
        query = self.getInputFromPort("query")
        url = self.getInputFromPort("url")
        result = esgf.fetchData(url);
        self.setResult("value", result)


# --------------------------------------------------------------------------fun
def initialize(*args, **keywords):

    # We'll first create a local alias for the module registry so that
    # we can refer to it in a shorter way.
    reg = core.modules.module_registry.registry

    reg.add_module(EsgfFilter)
    reg.add_input_port(EsgfFilter, "query",
                       (core.modules.basic_modules.String, 'the first argument'))
    reg.add_input_port(EsgfFilter, "url",
                       (core.modules.basic_modules.String, 'the second argument'))
    reg.add_output_port(EsgfFilter, "value",
                       (core.modules.basic_modules.List, 'the result'))
