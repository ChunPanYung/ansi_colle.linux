#!/usr/bin/env python3
import pytest
from testinfra.host import Host


@pytest.mark.linux
@pytest.mark.home_config
class TestPackage:
    @pytest.fixture
    def get_home(self, host: Host):
        return host.user("root").home

    def test_dir(self, host: Host, get_home: str):
        assert host.file("/tmp/RAM").is_directory
        assert host.file(get_home).is_directory
