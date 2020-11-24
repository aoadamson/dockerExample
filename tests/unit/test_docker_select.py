from controllers.docker_select import dockerSelect
import unittest


class DockerSelect(unittest.TestCase):

    def test_docker_select(self):
        result = dockerSelect()
        self.assertEqual(result, [('Austin',)])
