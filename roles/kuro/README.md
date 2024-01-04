ansi_colle.linux.powershell
=========

Install kuro (Microsoft ToDo for Linux) via Github and rpm.

Requirements
------------

NONE

Role Variables
--------------

```
kuro_github_api: >-
  https://api.github.com/repos/davidsmorais/kuro/releases/latest
```

Dependencies
------------

NONE

Example Playbook
----------------

```
- name: Example playbook
  hosts: all
  tasks:
    - name: Use this role
      ansible.builtin.include_role:
        name: ansi.colle.linux.kuro
```
