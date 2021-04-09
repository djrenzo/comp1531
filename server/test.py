import pytest

@pytest.mark.parametrize("y", [1, 1])
def test_foo(x, y):
    assert(x == y)

    
@pytest.fixture(params = ['CCDC',
	1,2,1])
def x(request):
	return request.param 
