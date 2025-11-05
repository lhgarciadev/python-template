from main import main


def test_main_prints_greeting(capsys):
    """main() should print the expected greeting to stdout."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from python-template!\n"


def test_main_is_callable():
    """The module exposes a callable `main` function."""
    import main as m

    assert hasattr(m, "main")
    assert callable(m.main)


def test_run_module_as_main(capsys):
    """Running the module as __main__ should also print the greeting (covers the module guard)."""
    import runpy

    # Execute the module as if run with `python -m main` / `python main.py`
    runpy.run_module("main", run_name="__main__")
    captured = capsys.readouterr()
    assert captured.out == "Hello from python-template!\n"
