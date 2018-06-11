from unittest.mock import mock_open

import pytest, os

from rmt.el.pytest_extra_learning import PytestExtraLearning


class TestPytestExtraLearning(object):
    @pytest.fixture()
    def target(self):
        return PytestExtraLearning()

    def test_simple(self, target):
        assert target.simple(), 'Northeastern University'

    def test_simple_mock(self, mocker, target):
        mock_logger = mocker.Mock(name="logger")
        target.simple_mock(mock_logger)
        mock_logger.debug('This is a test message').assert_called_once


    def test_forced_exception(self, target):
        with pytest.raises(ZeroDivisionError):
            target.forced_exception()

    def test_simple_patch(self, mocker, target):
        mocker.patch('os.remove')
        target.simple_patch('/tmp/foo')
        os.remove('/tmp/foo').assert_called_once

    def test_patch_object(self, mocker, target):
        mocker.patch('os.chroot')
        target.patch_object('/tmp/foo')
        os.chroot('/tmp/foo').assert_called_once

    def test_stub_object(self, mocker, target):
        stub = mocker.stub(name='thing')
        target.stub_object(stub)
        stub.assert_called_once_with('this', 'that')

    def test_spy_object(self, mocker, target):
        mocker.spy(target, 'spy_object')
        assert target.spy_object() == 'are you spying on me?'
        assert target.spy_object.call_count == 1

    def test_double_mock(self, mocker, target):
        mocker.patch('builtins.open', new_callable=mock_open, read_data='1')
        file = '/tmp/foo/file.txt'
        target.double_mock(file)
        assert target.double_mock(file) == '1'


if __name__ == '__main__':
    pytest.main()
