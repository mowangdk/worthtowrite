class A(list):
    def __get__(self, obj, cls):
        return 'A.__get__'

    def __set__(self, obj, value):
        print 'A.__set__'
        self.append(value)


class B(object):
    value = A()


if __name__ == '__main__':
    b = B()
    b.value = 1
    print b.__getattribute__('value')
    print b.value
    print b.__dict__['value']
    print b.__class__.__dict__['value']

