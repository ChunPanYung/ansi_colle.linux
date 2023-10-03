ansi_colle.linux.powershell
=========

Install powershell.

Requirements
------------

NONE

Role Variables
--------------

NONE

Dependencies
------------

NONE

Example Playbook
----------------

- name: Example playbook
  hosts: servers
  tasks:
    - name: Use this role
      ansible.builtin.include_role:
        name: ansi.colle.linux.powershell
