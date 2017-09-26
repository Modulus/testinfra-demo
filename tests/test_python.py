def test_runserver(host):
    pyfile = host.file("/demo/runserver.py")

    assert pyfile.exists
    assert pyfile.is_file
    assert pyfile.contains("app.run(host='0.0.0.0', debug=True)")
    assert oct(pyfile.mode) == "0o644"


#def test_socket(host):
#    socket = host.socket("tcp://0.0.0.0:5000")
#
#    assert socket.is_listening
