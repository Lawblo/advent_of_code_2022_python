import day09 as d


def test_move():
    assert (d.move_right([0, 0])) == [1, 0]
    assert (d.move_left([0, 0])) == [-1, 0]
    assert (d.move_up([0, 0])) == [0, 1]
    assert (d.move_down([0, 0])) == [0, -1]


def test_perform_move():
    assert (d.perform_move([0, 0], 'r')) == [1, 0]
    assert (d.perform_move([0, 0], 'l')) == [-1, 0]
    assert (d.perform_move([0, 0], 'u')) == [0, 1]
    assert (d.perform_move([0, 0], 'd')) == [0, -1]


def test_find_difference():
    assert (d.find_difference([0, 0], [0, 1])) == [0, -1]


def test_handle_difference():
    assert (d.handle_difference([2, 0], [0, 0])) == [1, 0]
    assert (d.handle_difference([2, 1], [0, 0])) == [1, 1]
    assert (d.handle_difference([2, -1], [0, 0])) == [1, -1]
    assert (d.handle_difference([2, 0], [0, 0])) == [1, 0]
    assert (d.handle_difference([2, 1], [0, 0])) == [1, 1]
    assert (d.handle_difference([2, -1], [0, 0])) == [1, -1]
