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

@pytest.mark.parametrize("a, b", [ (a,b) for a in np.linspace(0, 1, 20) for b in (0, 1, 20) ] )
def test_trougao(a, b):
    t = PravougliTrougao(a, b)
    assert t.povrsina() == a*b/2
    assert np.abs(t.obim() -  (a + b + np.sqrt(a**2 + b**2) ) ) < 1e-6

