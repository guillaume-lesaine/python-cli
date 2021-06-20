import pytest
from click.testing import CliRunner
from myclilibrary.interface import initdb


@pytest.mark.parametrize("name", [("toptoptop")])
def test_initdb(name):
    runner = CliRunner()
    result = runner.invoke(initdb, ["--name", name])

    if result.exit_code == 0:
        assert True
    else:
        raise result.exception


@pytest.mark.parametrize("name", [("oops")])
def test_initdb_exception(name):
    runner = CliRunner()
    result = runner.invoke(initdb, ["--name", name])

    with pytest.raises(ValueError):
        if result.exit_code == 0:
            pass
        else:
            raise result.exception
