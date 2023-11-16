# from collections import deque
#
#
# def math_operations_04_lab(*args, **kwargs):
#     args = deque(args)
#     result = []
#     final = []
#     for _ in range(len(args)):
#         if args:
#             kwargs["a"] += args.popleft()
#         if args:
#             kwargs["s"] -= args.popleft()
#         if args:
#             d = args.popleft()
#             if d != 0:
#                 kwargs["d"] /= d
#         if args:
#             kwargs["m"] *= args.popleft()
#
#     result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#
#     for k, v in result:
#         final.append(f"{k}: {v:.1f}")
#
#     return "\n".join(final)
def math_operations(*args, **kwargs):
    args = list(args)
    args_len = args
    result = []
    final = []
    for _ in range(len(args_len)):
        if args:
            kwargs["a"] += args.pop(0)
        if args:
            kwargs["s"] -= args.pop(0)
        if args:
            d = args.pop(0)
            if d != 0:
                kwargs["d"] /= d
        if args:
            kwargs["m"] *= args.pop(0)

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    for k, v in result:
        final.append(f"{k}: {v:.1f}")

    return "\n".join(final)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
