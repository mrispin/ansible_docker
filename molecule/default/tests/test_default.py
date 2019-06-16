import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_installed(host):
    docker = host.package("docker.io")
    assert docker.is_installed


def test_docker_group(host):
    dockergroup = host.group("docker")
    assert dockergroup.exists


def test_docker_service(host):
    dockerservice = host.service("docker")
    assert dockerservice.is_enabled
    assert dockerservice.is_running
