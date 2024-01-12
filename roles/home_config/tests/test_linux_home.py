#!/usr/bin/env python3
import pytest
from testinfra.host import Host


@pytest.mark.linux
@pytest.mark.home_config
class TestPackage:
    def test_home_dir(self, host: Host, get_home: str):
        assert host.file(f"{get_home}/.bashrc.d").is_directory

        assert host.file(f"{get_home}/.ssh").is_directory
        assert host.file(f"{get_home}/.gnupg").is_directory
        assert host.file(f"{get_home}/.keys").is_directory

        assert host.file(f"{get_home}/.local/bin").is_directory
        assert host.file(f"{get_home}/.local/opt").is_directory
        assert host.file(f"{get_home}/.local/script").is_directory
        assert host.file(f"{get_home}/.local/state").is_directory

        assert host.file(f"{get_home}/.config/systemd/user/").is_directory

        assert host.file(f"{get_home}/Repos/git").is_directory

    def test_home_file(self, host: Host, get_home: str):
        assert host.file(f"{get_home}/.bashrc").is_file
        assert host.file(f"{get_home}/.gitignore").is_file
        assert host.file(f"{get_home}/.gitconfig").is_file
        assert host.file(f"{get_home}/.bash_profile").is_file
