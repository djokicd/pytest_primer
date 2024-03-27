from mnogougao import *
import pytest 

@pytest.mark.parametrize("a", np.linspace(0, 10, 11))
def test_kvadrat(a):
    k = Kvadrat(a)
    assert k.povrsina() == a**2
    assert k.obim() == 4*a
