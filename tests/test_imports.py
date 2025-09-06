def test_import_package() -> None:
    import oclius

    assert isinstance(oclius.__version__, str) and len(oclius.__version__) > 0
