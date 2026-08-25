from hello_agent import main


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "Hello from hello-agent!\n"