import logging
import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):                          # WILL CREATE LOGGER ON CLASS LEVEL
        self.log.debug('debug message')         # LoggingDemo2.log
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2Log = cl.customLogger(logging.INFO)   # WILL CREATE SEPARATE LOGGER
        m2Log.debug('debug message')            # FILE FOR method2 -(method2.log)
        m2Log.info('info message')
        m2Log.warn('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    def method3(self):                          # WILL CREATE SEPARATE LOGGER
        m3Log = cl.customLogger(logging.INFO)   # FILE FOR method3 -(method3.log)
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warn('warn message')
        m3Log.error('error message')
        m3Log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()