import os

class PytestExtraLearning(object):

    @staticmethod
    def simple():
        return 'Northeastern University'

    @staticmethod
    def simple_mock(logger):
        logger.debug('This is a test message')

    @staticmethod
    def forced_exception():
        1 / 0

    @staticmethod
    def simple_patch(path):
        os.remove(path)

    @staticmethod
    def patch_object(path):
        os.chroot(path)

    @staticmethod
    def stub_object(thing):
        thing('this', 'that')

    @staticmethod
    def spy_object():
        return 'are you spying on me?'

    @staticmethod
    def double_mock(file):
        with open(file) as reader:
            value = reader.read(1)

        return value
