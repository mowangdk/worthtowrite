
def iteractive_iter(a):
    for i in a:
        a2 = yield i
        if a2:
            it = iteractive_iter(a2)
            a3 = None
            while 1:
                try:
                    a3 = yield it.send(a3)
                except StopIteration:
                    break


def main():
    iteration = iteractive_iter([1, 2, 3, 4, 5])
    i = iteration.send(None)
    print i
    for i in range(2):
        text = iteration.send([])
        print text



if __name__ == '__main__':
    main()