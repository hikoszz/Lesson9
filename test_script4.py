import script4

class Testadd:
    def test_add_2_2(self):
        assert script4.add(2, 2) == 4
    def test_add_12_12(self):
        assert script4.add(12, 12) == 24
    
    
class Testsub:
    def test_sub_4_2(self):
        assert script4.sub(4, 2) == 2
    def test_sub_10_2(self):
        assert script4.sub(10, 2) == 8

class Testpow:
    def test_pow_2_2(self):
        assert script4.pow(2, 2) == 4
    def test_pow_2_2(self):
        assert script4.pow(12, 12) == 144

class Testcel:
    def test_cel_10_3(self):
        assert script4.cel(10, 3) == 1
    def test_cel_10_3(self):
        assert script4.cel(5, 2) == 1

