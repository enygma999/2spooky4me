import operator
import re
import sys
from typing import Callable

OP_SYMBOLS: dict[str, Callable[[int, int], int]] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
}


def main(in_string: str, op_string: str) -> str:
    operation: Callable[[str], str] = create_op_func(op_string)
    out_string: str = in_string
    for number in set(re.findall(r'\d+', in_string)):
        out_string = out_string.replace(number, operation(number))
    return out_string


def create_op_func(op_string: str) -> Callable[[str], str]:
    operations: list[str] = re.findall(r"[+\-/*^]\d+", op_string)
    if "".join(operations) != op_string:
        raise ValueError(f"Operation '{op_string}' is not valid")

    def op_func(number: str) -> str:
        int_number: int = int(number)
        for operation in operations:
            int_number = OP_SYMBOLS[operation[0]](
                int_number, int(operation[1:]))
        return str(int_number)

    return op_func


if __name__ == '__main__':
    print(main(*sys.argv[1:3]))
