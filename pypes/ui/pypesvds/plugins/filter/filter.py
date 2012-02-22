import logging
import traceback

from pypes.component import Component

log = logging.getLogger(__name__)

class Filter(Component):
    # defines the type of component we're creating.
    __metatype__ = 'TRANSFORMER'

    def __init__(self):
        # initialize parent class
        Component.__init__(self)
        
        # Optionally add/remove component ports
        # self.remove_output('out')
        # self.add_input('in2', 'A description of what this port is used for')

        locs = ["World", "Asia", "Africa", "North America", "South America", 
                "Antarctica", "Europe", "Australia"
                "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

        self.remove_input('in')
        self.remove_output('out')
        self.add_input('source', '(edu.utah.sci.vistrails.basic:String)')
        self.add_output('files', '(edu.utah.sci.vistrails.basic:File)')

        self.set_parameter('From', '1/1/1900', None, 'edu.utah.sci.vistrails.basic:Date')
        self.set_parameter('To   ', '12/31/2012', None, 'edu.utah.sci.vistrails.basic:Date')
        self.set_parameter('Location','World', locs, 'edu.utah.sci.vistrails.basic:String')
        self.set_parameter('MaxItems','1', None, 'edu.utah.sci.vistrails.basic:Integer')
        self.set_package('edu.utah.sci.vistrails.http')
        self.set_version('0.0.1')

        # Setup any user parameters required by this component 
        # 2nd arg is the default value, 3rd arg is optional list of choices
        #self.set_parameter('MyParam', 'opt1', ['opt1', 'opt2', 'opt3'])

        # log successful initialization message
        log.info('Component Initialized: %s' % self.__class__.__name__)

    def run(self):
        # Define our components entry point
        while True:

            # myparam = self.get_parameter('MyParam')             

            # for each document waiting on our input port
            for doc in self.receive_all('in'):
                try:
                    # perform your custom logic here
                    pass
                except Exception as e:
                    log.error('Component Failed: %s' % self.__class__.__name__)
                    log.error('Reason: %s' % str(e))                    
                    log.error(traceback.print_exc())

                # send the document to the next component
                self.send('out', doc)

            # yield the CPU, allowing another component to run
            self.yield_ctrl()

