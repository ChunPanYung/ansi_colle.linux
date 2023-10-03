# ansi_colle
Collection of roles and plugins for personal use.
There is multiple ways to use this repo.

This collections assume user configure/connect to remote Windows host using SSH.
For more information how to setup, Execute/look at `Setup-SSH.ps1` in this directory.

## Install via CLI
To install the all collection from this repo:
```
ansible-galaxy collection install \
    git+https://{{ repo link }}.git#/{{ collection }},{{ branch_name }}
```

## `Requirements.yml`
Add the following into your `requirements.yml`:
```
---
collections:
  - name: https://{{ repo link }}#/{{ collection_name }}
    type: git
    version: {{ branch name }}
```

You can then run: `ansible-galaxy install -r requirements.yml`

## Playbook
You can also install via playbook:
```
---
- name: Install collections
  hosts: localhost  # Server that will run this playbook
  tasks:
    - name: Install one collection from repo
      community.general.ansible_galaxy_install:
        type: collection
        name: git+{{ repo link }}.git#/{{ collection name }},{{ branch name }}

    - name: Install all collections from repo
      community.general.ansible_galaxy_install:
        type: collection
        name: git+{{ repo link }}.git,{{ branch name }}
```
