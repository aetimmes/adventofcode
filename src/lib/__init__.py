from typing import Union

DIRS8: dict[str, tuple[int, int]] = {
    "E": (0, 1),
    "SE": (1, 1),
    "S": (1, 0),
    "SW": (1, -1),
    "W": (0, -1),
    "NW": (-1, -1),
    "N": (-1, 0),
    "NE": (-1, 1),
}

DIRS4 = {c: DIRS8[c] for c in "ESWN"}


def bci(r, c, mr, mc: int) -> bool:
    """boundscheck ints"""
    return (0 <= r < mr) and (0 <= c < mc)


def bcg(r: int, c: int, g: Union[list, str]) -> bool:
    """boundscheck ints+grid"""
    if isinstance(g, str):
        g = g.splitlines()
    mr, mc = len(g), len(g[0])
    return (0 <= r < mr) and (0 <= c < mc)


def bcdg(
    p: tuple[int, int], d: Union[str, tuple[int, int]], g: Union[str, list[str]]
) -> bool:
    """boundscheck tuples+grid"""
    if isinstance(d, str):
        d = DIRS8[d]
    if isinstance(g, str):
        g = g.splitlines()
    m = (len(g), len(g[0]))
    return all((0 <= p[i] + d[i] < m[i] for i in (0, 1)))


def step(p: tuple[int, int], d: Union[str, tuple[int, int]]) -> tuple[int, int]:
    """take a step"""
    if isinstance(d, str):
        d = DIRS8[d]
    return (p[0] + d[0], p[1] + d[1])
