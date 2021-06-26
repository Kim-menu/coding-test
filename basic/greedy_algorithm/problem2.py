def is_add_condition(a, b):
    operand_set = {a, b}
    if 0 in operand_set or 1 in operand_set: return True
    return False

Operands = tuple(map(int, input()))
Result = Operands[0]
for Index in range(1, len(Operands)):
    if is_add_condition(Result, Operands[Index]):
        Result += Operands[Index]
    else:
        Result *= Operands[Index]
print(Result)