from copy import deepcopy

import pykube

from . import BASE_CONFIG, TestCase


class TestAuthExecPlugin(TestCase):
    def setUp(self):
        cfg = deepcopy(BASE_CONFIG)
        cfg.update({
            'users': [
                {
                    'name': 'test-user',
                    'user': {
                        'exec': {
                            'command': 'heptio-authenticator-aws',
                            'args': [
                                "token",
                                "-i",
                                "test-pykube-mock-eks-cluster"
                            ],
                        },
                    },
                },
            ]
        })
        self.config = pykube.KubeConfig(doc=cfg)

    def test_authexecplugin_builds_command(self):
        plugin = pykube.http.AuthExecPlugin(self.config)
        assert plugin.command == ["heptio-authenticator-aws", "token", "-i", "test-pykube-mock-eks-cluster"]
