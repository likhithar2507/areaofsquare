import Dimension

def test_areaofsquare():
    side=2
    result=Dimension.areaofsquare()
    assert result==side**2
@pytest.mark.perimeteareaofsquare
def test_perimeterofrectangle():
    length =2
    breadth=2
    result=Dimension.perimeterofrectangle()
    assert result==2*(length + breadth)

@pytest.mark.perimeterandareaofrectangle
def test_areaofrectangle():
    length = 2
    breadth = 2
    result=Dimension.areaofrectangle()
    assert result==length*breadth



