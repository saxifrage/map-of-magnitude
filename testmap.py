import genmap


def test_map_can_draw_an_empty_canvas():
    m = genmap.MagnitudeMap(canvas_size=(32, 8), sum_of_magnitudes=0)
    assert unicode(m) == """\
----------------------------------------
----------------------------------------
----------------------------------------
----------------------------------------
----                                ----
----                                ----
----                                ----
----                                ----
----                                ----
----                                ----
----                                ----
----                                ----
----------------------------------------
----------------------------------------
----------------------------------------
----------------------------------------"""


def test_map_can_draw_an_empty_canvas_with_different_alleys():
    m = genmap.MagnitudeMap(canvas_size=(32, 8), alley_width=2)
    assert unicode(m) == """\
------------------------------------
------------------------------------
--                                --
--                                --
--                                --
--                                --
--                                --
--                                --
--                                --
--                                --
------------------------------------
------------------------------------"""


# find_first_empty_cell - ffec

def test_ffec_finds_first_empty_cell():
    m = genmap.MagnitudeMap(canvas_size=(12, 4), sum_of_magnitudes=10, alley_width=2)
    assert m.find_first_empty_cell() == (2, 2)
