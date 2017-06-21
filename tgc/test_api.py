import unittest

from app import app as tgc

class APITestCase(unittest.TestCase):

    def setUp(self):
        tgc.config['TESTING'] = True
        self.app = tgc.test_client()

    def tearDown(self):
        pass

    def test_calculate(self):
        resp = self.app.get('/calculate?x=1')
        assert 'undefined' in resp.data

if __name__ == '__main__':
    unittest.main()