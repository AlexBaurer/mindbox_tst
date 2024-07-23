from mindbox_tst.sqr_calc import figure_sqr


def test_sqr_circle_types():
    """Test diff types"""
    # test list
    res_1 = figure_sqr([2])
    expected_1 = 12.57

    # test int
    res_2 = figure_sqr(3)
    expected_2 = 28.27

    assert res_1 == expected_1
    assert res_2 == expected_2


def test_sqr_triangle():
    """Test triangle square calculating"""
    c = 0
    inputs = [[2, 3, 4], [12, 23, 25], [4, 6, 8]]
    results = [2.90, 137.48, 11.62]

    for el in inputs:
        res = figure_sqr(el)
        assert res == results[c]
        c += 1



