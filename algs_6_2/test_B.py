import dataclasses
import pytest

from task_B import get_socks_and_shirts


##################
# TEST FOR TASK B
##################


@dataclasses.dataclass
class Case:
    blue_shirt: int
    red_shirt: int
    blue_sock: int
    red_sock: int
    result: tuple[int]

    def __str__(self) -> str:
        return f"shirts_and_soks_{self.result}"


TEST_CASES = [
    Case(blue_shirt=6, red_shirt=2, blue_sock=7, red_sock=3, result=(3, 4)),
    Case(blue_shirt=10, red_shirt=0, blue_sock=5, red_sock=3, result=(1, 4)),
    Case(blue_shirt=10, red_shirt=0, blue_sock=1, red_sock=13, result=(1, 14)),
    Case(blue_shirt=1, red_shirt=1, blue_sock=1, red_sock=1, result=(2, 1)),
    Case(blue_shirt=1, red_shirt=1, blue_sock=7, red_sock=3, result=(2, 1)),
    Case(blue_shirt=10, red_shirt=10, blue_sock=15, red_sock=15, result=(11, 1)),
    Case(blue_shirt=10, red_shirt=10, blue_sock=7, red_sock=3, result=(11, 1)),
    Case(blue_shirt=8, red_shirt=9, blue_sock=5, red_sock=9, result=(10, 1)),
    Case(blue_shirt=8, red_shirt=9, blue_sock=8, red_sock=9, result=(10, 1)),
    Case(blue_shirt=10, red_shirt=2, blue_sock=2, red_sock=10, result=(11, 1)),
    Case(blue_shirt=1, red_shirt=2, blue_sock=2, red_sock=1, result=(3, 1)),
    Case(blue_shirt=114, red_shirt=299, blue_sock=921, red_sock=166, result=(300, 1)),
    Case(blue_shirt=790, red_shirt=493, blue_sock=507, red_sock=302, result=(1, 508)),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_tree_painter(t: Case) -> None:
    result = get_socks_and_shirts(t.blue_shirt, t.red_shirt, t.blue_sock, t.red_sock)
    assert result == t.result
