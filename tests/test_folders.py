def test_demo_newspaperdemo_folder(host):
    folder = host.file("/demo/newspaperdemo")

    assert folder.exists
    assert folder.is_directory

def test_requirements_file(host):
    req_file = host.file("/demo/requirements.txt")

    assert req_file.exists
    assert req_file.is_file
    assert req_file.contains("BeautifulSoup==")
    assert req_file.contains("Flask==")
    assert req_file.contains("Jinja2==")
    assert req_file.contains("MarkupSafe==")
    assert req_file.contains("Pillow==")
    assert req_file.contains("Werkzeug==")
    assert req_file.contains("argparse==")
