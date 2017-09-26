def test_os(host):
    info = host.system_info

    assert info.type == "linux"
    assert info.distribution == "debian"
    assert info.release == "8"
