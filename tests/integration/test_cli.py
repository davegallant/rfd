from subprocess import Popen, PIPE
import pytest


def run_cli(args, timeout=15):
    cmd = ["python", "-m", "rfd"] + args.split()
    p = Popen(cmd, stdout=PIPE)
    stdout, _ = p.communicate(timeout=timeout)
    assert p.returncode == 0
    return stdout


def test_version():
    stdout = run_cli("--version")
    assert b"rfd v" in stdout


@pytest.mark.parametrize("args", ["", "--sort-by score"])
def test_threads(args):
    run_cli("threads " + args)


@pytest.mark.parametrize("args", ["'pizza'", "'(coffee|starbucks)'"])
def test_search(args):
    run_cli("search " + args)
