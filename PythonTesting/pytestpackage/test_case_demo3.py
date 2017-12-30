# Open Terminal in Pycharm
# cd pytestpackage/
# py.test -v -s test_case_demo3.py
import  pytest

# @pytest.fixture()  to run before every method if specified

@pytest.yield_fixture() # to run before and after every method if specified
def setUp():
    print("Running demo3 setUp")
    yield
    print("Running demo3 tearDown")

def test_demo3_methodA(setUp):
    print("Running demo3 method A")


def test_demo3_methodB(setUp):
    print("Running demo3 method B")

# to run all tests in pytestpackage:
    # Open Terminal in Pycharm
    # cd pytestpackage/
    # py.test -v -s

# to run only one test(methodA) from test_case_demo3:
    # Open Terminal in Pycharm
    # cd pytestpackage/
    # py.test -v -s test_case_demo3.py::test_demo3_methodA