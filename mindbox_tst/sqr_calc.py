from mindbox_tst.figure_classes import *


def figure_sqr(figure: list | int, measure: str = 'meters') -> float:
    """Send list of 1 element for circle; of 3 elements for triangle
     as first argument and unit of measurement as second"""

    if type(figure) == int:
        figure = [figure]

    if len(figure) == 1:
        fig = FCircle(figure)
        return fig.calc_sqr(measure)
    elif len(figure) == 2:
        print("This figure cannot have a measurable square")
    elif len(figure) == 3:
        fig = FTriangle(figure)
        return fig.calc_sqr(measure)
    else:
        pass

