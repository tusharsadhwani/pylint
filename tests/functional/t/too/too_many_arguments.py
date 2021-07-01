# pylint: disable=missing-docstring,wrong-import-position,too-few-public-methods

def stupid_function(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):  # [too-many-arguments]
    return arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9


class MyClass:
    text = "MyText"

    def mymethod1(self):
        return self.text

    def mymethod2(self):
        return self.mymethod1.__get__(self, MyClass)


MyClass().mymethod2()()


# Check a false positive does not occur
from functools import partial


def root_function(first, second, third):
    return first + second + third


def func_call():
    """Test we don't emit a FP for https://github.com/PyCQA/pylint/issues/2588"""
    partial_func = partial(root_function, 1, 2, 3)
    partial_func()
    return root_function(1, 2, 3)


class NoParentClass:  # pylint: disable=too-many-arguments
    """Test for https://github.com/PyCQA/pylint/issues/1191"""
    def __init__(self, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
        self.arg_4 = arg_4
        self.arg_5 = arg_5
        self.arg_6 = arg_6

class Base:
    pass


class ChildOfBase(Base):  # pylint: disable=too-many-arguments
    """Test for https://github.com/PyCQA/pylint/issues/1191"""
    def __init__(self, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
        self.arg_4 = arg_4
        self.arg_5 = arg_5
        self.arg_6 = arg_6
