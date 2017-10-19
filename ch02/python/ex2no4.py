nums = range(10)    # 0から10までの配列
print(nums)
odd_squares = [x * x for x in nums if x % 2]    # 配列から１つずつ取り出し、要素×要素を計算。ただし、２で割って余る（＝奇数）数の場合のみ。
print(odd_squares)
print(sum(odd_squares))

def is_odd(x):
    return x%2

def sq(x):
    return x * x

print(sum([sq(x) for x in nums if is_odd(x)]))