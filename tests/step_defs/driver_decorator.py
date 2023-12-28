from tests.step_defs.i_driver import IDriver

"""
The Decorator also implements the IComponent
To add a similar logging capability for the CoreDriver
"""


class DriverDecorator(IDriver):
    # @staticmethod
    # def implicitly_wait(config_wait_time):
    #     pass

    @staticmethod
    def start(browser):
        pass

    @staticmethod
    def findElement(self):
        pass
