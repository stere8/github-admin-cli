def test_cli_help(temp_path):
    import subprocess
    subprocess.run(['ghadmin --help'],check=True)