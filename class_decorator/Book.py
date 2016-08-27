import numbers


# ensure函数会以给定的属性名,验证器函数以及可选的docstring为参数来创造类修饰器
def ensure(name, validate, doc=None):
    def decorator(Class):
        privateName = '__'+name

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            validate(name, value)
            return setattr(self, privateName, value)
        setattr(Class, name, property(getter, setter, doc=doc))
        return Class
    return decorator


# 这个验证器是用来确保book和title的属性不是空字符串
def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} must be type of str".format(name))
    if not bool(value):
        raise ValueError("{} may not be empty".format(name))


# 这个函数是一个工厂函数,每次调用的时候就会创建新的验证器函数
def is_in_range(minimum=None, maxinum=None):
    assert minimum is not None or maxinum is not None

    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} must be a number".format(name))
        if minimum is not None and value < minimum:
            raise ValueError("{},{} is too small".format(name, value))
        if maxinum is not None and value > maxinum:
            raise ValueError("{},{} is too big".format(name, value))
    return is_in_range


@ensure('title', is_non_empty_str)
@ensure('price', is_in_range(1, 10000))
@ensure('title', is_in_range(0, 1000000))
class Book(object):
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity


