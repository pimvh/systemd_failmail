import testinfra


def test_systemd_failmail_global_dependency_exists(host):
    """test that the global dependency is present"""

    assert host.file("/etc/systemd/system/service.d/10-all.conf")


def Test_systemd_failmail_service_exists(host):
    """test that the systemd failmail service exists"""

    assert host.file("/etc/systemd/system/failmail@.service")
