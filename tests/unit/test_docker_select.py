from controllers.docker_select import docker_select
import unittest


class DockerSelect(unittest.TestCase):

    def test_docker_select(self):
        result = docker_select()
        self.assertEqual(result, [('Austin',)])
