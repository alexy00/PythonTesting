# Open Terminal in Pycharm
# cd pytestpackage/
# py.test -v -s test_case_demo2.py
import  pytest

# @pytest.fixture()  to run before every method if specified

@pytest.yield_fixture() # to run before and after every method if specified
def setUp():
    print("Running demo2 setUp")
    yield
    print("Running demo2 tearDown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")


def test_demo2_methodB(setUp):
    print("Running demo2 method B")