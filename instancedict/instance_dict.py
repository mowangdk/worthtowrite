class A(object):
    def test1(self, text):
        print text


class B(A):
    def __init__(self, start):
        self.start = start

    def test2(self, text):
        print text


if __name__ == '__main__':
    b = B("a")
    b.test2("yao")
    b.test1("yao1")
    print b.__dict__
