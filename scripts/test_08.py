import allure
class Test_001:
    @allure.step(title="第一个测试")
    def test_001_1(self):
        assert 0
    @allure.step(title="第二个测试")
    def test_001_2(self):
        assert 1