from pathlib import Path
from time import time
from off_version import main


def test_oioioi(input_path):
    output_path = input_path.with_suffix(".out")
    with output_path.open() as fd:
        expected_result = [i.rstrip() for i in fd]
    with input_path.open() as fd:
        raw_result = main(fd)
    result = list(map(str, raw_result))
    assert result == expected_result


def pytest_generate_tests(metafunc):
    test_path = Path(__file__).parent.joinpath("tests")
    paths = list(test_path.glob("*.in"))
    metafunc.parametrize("input_path", paths, ids=[p.stem for p in paths])
