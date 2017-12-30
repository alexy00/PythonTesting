import logging
import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):                          # TO CREATE SAME LOGGER FILE FOR ALL
        self.log.debug('debug message')         # METHODS (LoggingDemo2.log)
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method3(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()