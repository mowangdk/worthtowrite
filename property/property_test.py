class Test(object):
    @property
    def get_fee(self):
        return self.fee

    # 也可以使用.delete
    @get_fee.setter
    def set_fee(self, value):
        self.fee = value


if __name__ == '__main__':
    t = Test()
    t.fee = 'py'
    print t.fee
