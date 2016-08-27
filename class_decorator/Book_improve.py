import numbers


def do_ensure(Class):
    def make_property(name, attribute):
        private_name = "__"+name
        def getter(self):
            return getattr(self, private_name)
        def setter(self, value):
            attribute.validate(name, value)
            return setattr(self, private_name, value)
        return property(getter, setter, doc=attribute.doc)
    for name, attribute in Class.__dict__.items():
        if isinstance(attribute, Ensure):
            setattr(Class, name, make_property(name, attribute))
    return Class


@do_ensure
class Book:
    title = Ensure(is_non_empty_str)
    price = Ensure(is_in_range(1, 10000))
    quantity = Ensure(is_in_range(0, 1000000))

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity


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


class Ensure(object):
    def __init__(self, validate, doc=None):
        self.validate = validate
        self.doc = doc




