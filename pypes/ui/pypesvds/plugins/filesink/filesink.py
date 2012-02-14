import logging
import traceback

from pypes.component import Component

log = logging.getLogger(__name__)

class FileSink(Component):
    # defines the type of component we're creating.
    __metatype__ = 'PUBLISHER'

    def __init__(self):
        # initialize parent class
        Component.__init__(self)
        
        # Optionally add/remove component ports
        self.remove_output('out')
        self.remove_input('in')
        self.add_input('file')

        self.set_parameter('outputPath', '')
        self.set_parameter('file', '')

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

