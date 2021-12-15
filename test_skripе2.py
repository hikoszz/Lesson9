import auto

class Test_adder():
    def test_adder_max(self):
        assert auto.adder(10000000, 12457841) == 100000
    def test_adder_min(self):
        assert auto.adder(1, -12) == 0
    def test_adder_1(self):
        assert auto.adder(0, 0) == "Net chisel dlya slogeniya"