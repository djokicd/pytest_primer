from mnogougao import *
import pytest 
 
@pytest.mark.parametrize("a", np.linspace(-10, 10, 21))
def test_kvadrat(a):
    try:
        k = Kvadrat(a)
        assert k.povrsina() == a**2
        assert k.obim() == 4*a
    except ValueError as e:
        assert a < 0