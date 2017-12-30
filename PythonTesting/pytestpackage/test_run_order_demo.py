# Open Terminal in Pycharm
# cd pytestpackage/
# py.test -v -s test_run_order_demo.py
import  pytest


# @pytest.fixture()  to run before every method if specified


@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Running method D")

@pytest.mark.run(order=4)
def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Running method E")

@pytest.mark.run(order=6)
def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Running method F")