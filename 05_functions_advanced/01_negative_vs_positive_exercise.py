def n_sums(*args):
    # option n1 is the most optimized
    # neg_sum = 0
    # pos_sum = 0
    # for num in args:
    #     if num > 0:
    #         pos_sum += num
    #     else:
    #         neg_sum += num

    #
    # neg_sum = sum([x for x in args if x < 0])
    # pos_sum = sum(([x for x in args if x > 0]))

    neg_sum = sum(list(filter(lambda x: x < 0, args)))
    pos_sum = sum(list(filter(lambda x: x > 0, args)))
    return neg_sum, pos_sum


n = [int(x) for x in input().split()]
neg, pos = n_sums(*n)

print(neg)
print(pos)
if abs(neg) > abs(pos):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
