Ansible: docker
===============

[![Build Status](https://travis-ci.org/mrispin/ansible_docker.svg?branch=master)](https://travis-ci.org/mrispin/ansible_docker)

Install docker.

Requirements
------------

None

Role Variables
--------------

### docker\_users
A list of users that are given permissions to manage docker

    docker-users:
      - user1
      - user2


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        docker_users:
          - user1
          - user2
      roles:
         - docker

License
-------

BSD

