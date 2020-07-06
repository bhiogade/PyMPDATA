"""
Created at 11.10.2019

@author: Piotr Bartman
@author: Michael Olesik
@author: Sylwester Arabas
"""

from MPyDATA.factories import Factories
from MPyDATA.options import Options
import pytest
import numpy as np

# test data by Dorota Jarecka
# see http://dx.doi.org/10.3233/SPR-140379
params = (
    (3, 3, 0.1, 0.5, 1, 1,
     np.array([[0., 0., 0.],
               [0., 0., 0.],
               [0., 0., 1.]]),
     np.array([[0., 0., 0.1],
               [0., 0., 0.],
               [0.5, 0., 0.4]])
     ),
    (3, 3, 0.1, 0.5, 1, 2,
     np.array([[0., 0., 0.],
               [0., 0., 0.],
               [0., 0., 1.]]),
     np.array([[0., 0., 0.0921],
               [0., 0., 0.],
               [0.5011, 0., 0.4068]])
     ),
    (3, 3, 0.2, 0.2, 1, 1,
     np.array([[0., 0., 0.],
               [0., 1., 0.],
               [0., 1., 0.]]),
     np.array([[0., 0.2, 0.],
               [0., 0.6, 0.2],
               [0., 0.8, 0.2]])
     ),
    (3, 3, 0.2, 0.2, 1, 2,
     np.array([[0., 0., 0.],
               [0., 1., 0.],
               [0., 0., 0.]]),
     np.array([[0., 0., 0.],
               [0., 0.64, 0.18],
               [0., 0.18, 0.]])
     ),
    (3, 3, 0.2, 0.2, 1, 3,
     np.array([[0., 0., 0.],
               [0., 1., 0.],
               [0., 0., 0.]]),
     np.array([[0., 0., 0.],
               [0., 0.6578, 0.1711],
               [0., 0.1711, 0.]])
     ),
    (3, 3, 0.5, 0.5, 1, 1,
     np.array([[0., 0., 0.],
               [0., 1., 0.],
               [0., 0., 0.]]),
     np.array([[0., 0., 0.],
               [0., 0., 0.5],
               [0., 0.5, 0.]])),
    (3, 3, 0.5, 0.5, 1, 2,
     np.array([[0., 0., 0.],
               [0., 1., 0.],
               [0., 0., 0.]]),
     np.array([[0., 0., 0.],
               [0., 0., 0.5],
               [0., 0.5, 0.]])
     ),
    (3, 3, 0.5, 0.5, 1, 3, np.array([[0., 0., 0.],
                                     [0., 1., 0.],
                                     [0., 0., 0.]]), np.array([[0., 0., 0.],
                                                               [0., 0., 0.5],
                                                               [0., 0.5, 0.]])),
    (3, 3, 0.0, 1.0, 3, 1, np.array([[0., 0., 0.],
                                     [0., 1., 0.],
                                     [0., 0., 0.]]), np.array([[0., 0., 0.],
                                                               [0., 1., 0.],
                                                               [0., 0., 0.]])),
    (3, 3, 0.0, 1.0, 3, 2, np.array([[0., 0., 0.],
                                     [0., 1., 0.],
                                     [0., 0., 0.]]), np.array([[0., 0., 0.],
                                                               [0., 1., 0.],
                                                               [0., 0., 0.]])),
    (3, 3, 0.0, 1.0, 3, 3, np.array([[0., 0., 0.],
                                     [0., 1., 0.],
                                     [0., 0., 0.]]), np.array([[0., 0., 0.],
                                                               [0., 1., 0.],
                                                               [0., 0., 0.]])),
    (3, 3, 1.0, 0.0, 4, 1, np.array([[0., 0., 0.],
                                     [0., 0., 0.],
                                     [0., 1., 0.]]), np.array([[0., 1., 0.],
                                                               [0., 0., 0.],
                                                               [0., 0., 0.]])),
    (3, 3, 1.0, 0.0, 4, 2, np.array([[0., 0., 0.],
                                     [0., 0., 0.],
                                     [0., 1., 0.]]), np.array([[0., 1., 0.],
                                                               [0., 0., 0.],
                                                               [0., 0., 0.]])),
    (3, 3, 1.0, 0.0, 4, 3, np.array([[0., 0., 0.],
                                     [0., 0., 0.],
                                     [0., 1., 0.]]), np.array([[0., 1., 0.],
                                                               [0., 0., 0.],
                                                               [0., 0., 0.]])),
    (4, 4, 0.5, 0.5, 1, 1, np.array([[0., 0., 0., 0.],
                                     [0., 0., 0., 0.],
                                     [0., 0., 0., 0.],
                                     [0., 0., 0., 1.]]), np.array([[0., 0., 0., 0.5],
                                                                   [0., 0., 0., 0.],
                                                                   [0., 0., 0., 0.],
                                                                   [0.5, 0., 0., 0.]])),
    (4, 4, 0.5, 0.5, 1, 2, np.array([[0., 0., 0., 0.],
                                     [0., 0., 0., 0.],
                                     [0., 0., 0., 0.],
                                     [0., 0., 0., 1.]]), np.array([[0., 0., 0., 0.5],
                                                                   [0., 0., 0., 0.],
                                                                   [0., 0., 0., 0.],
                                                                   [0.5, 0., 0., 0.]])),
    (4, 4, 0.5, 0.5, 1, 3, np.array([[0., 0., 0., 0.],
                                     [0., 0., 0., 0.],
                                     [0., 0., 0., 0.],
                                     [0., 0., 0., 1.]]), np.array([[0., 0., 0., 0.5],
                                                                   [0., 0., 0., 0.],
                                                                   [0., 0., 0., 0.],
                                                                   [0.5, 0., 0., 0.]])),
    (10, 1, 1.0, 0.0, 5, 1, np.array([1., 0., 1., 0., 0., 0., 0., 0., 0., 0.]),
        np.array([0., 0., 0., 0., 0., 1., 0., 1., 0., 0.])))


@pytest.fixture(params=params)
def case(request):
    return request.param


class TestMPDATA2D:
    def test_Arabas_et_al_2014_sanity(self, case):
        case = {
            "nx": case[0],
            "ny": case[1],
            "Cx": case[2],
            "Cy": case[3],
            "nt": case[4],
            "ni": case[5],
            "input": case[6],
            "output": case[7]
        }
        # Arrange
        sut = Factories.constant_2d(
            case["input"].reshape((case["nx"], case["ny"])),
            [case["Cx"], case["Cy"]],
            options=Options(n_iters=case["ni"])
        )

        # Act
        sut.advance(nt=case["nt"])

        # Assert
        np.testing.assert_almost_equal(sut.advectee.get(), case["output"].reshape(case["nx"], case["ny"]), decimal=4)
