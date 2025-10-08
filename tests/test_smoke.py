def test_cli_help():
    import subprocess
    subprocess.run(['ghadmin', '--help'],check=True)