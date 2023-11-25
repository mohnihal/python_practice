class Test:
    def _decorator(foo):
        def magic(cls) :
            print("start magic")
            foo(cls)
            print("end magic")
        return magic

    @classmethod
    @_decorator
    def bar(cls) :
        print("normal call")


Test.bar()