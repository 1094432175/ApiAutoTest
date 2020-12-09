class TestAdd:
    def test_001(self,):#这里执行前置
        print("添加:用例1")
    def test_002(self):
        print("添加:用例2")
    def test_003(self,login):
        print("添加:用例3")#这里执行后置