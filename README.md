Role Name
=========

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

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

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

