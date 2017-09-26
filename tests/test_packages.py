def test_python_pkg(host):
    pkg = host.package("python")

    assert pkg.is_installed
