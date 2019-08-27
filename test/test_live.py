from pygns3 import *
import unittest
from loguru import logger


class TestLive(unittest.TestCase):
    def test_simple(self):
        GNS3API.load_configuration()

        controller = GNS3Controller()
        logger.debug({'Controller': controller})
        logger.debug({'Computes': [c.name for c in controller.computes]})
        logger.debug({'Projects': [proj.name for proj in controller.projects]})

        project = GNS3Project.from_name(name='switch-ladder-1')

        logger.debug({'Project': project})
        logger.debug({'Drawings': project.drawings})
        logger.debug({'Nodes': project.nodes})
        logger.debug({'Links': project.links})
        logger.debug({'Snapshots': project.snapshots})

        node = project.nodes[0]
        logger.debug({node.name: node.properties})



