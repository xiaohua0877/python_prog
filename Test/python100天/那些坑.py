x = y = 0
while True:
    x -= 1
    y -= 1
    if x is y:
        print('%d is %d' % (x, y))
    else:
        print('Attention! %d is not %d' % (x, y))
        break



names = ['关羽', '张飞', '赵云', '马超', '黄忠']
subjs = ['语文', '数学', '英语']
scores = [[0] * 3 for _ in range(5)]
for row, name in enumerate(names):
    print('请输入%s的成绩' % name)
    scores[row] = [0] * 3
    for col, subj in enumerate(subjs):
        scores[row][col] = float(input(subj + ': '))
print(scores)