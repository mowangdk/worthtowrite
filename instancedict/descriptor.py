class A(list):
    def __get__(self, object, cls):
        return 'A.__get__'


class B(object):
    value = A()


def work1():
    b = B()
    print b.value
    s = b.value
    type(s)


def work2():
    b = B()
    b.value = 1
    print b.__dict__['value']
    print b.__class__.__dict__['value']


if __name__ == '__main__':
    work1()
    work2()
