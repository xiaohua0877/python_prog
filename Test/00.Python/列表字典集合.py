###列表、字典、集合、元组的使用
from random import randint, sample

# 列表解析
data = [randint(-10, 10) for _ in xrange(10)]

filter(lambda x: x >= 0, data)
[x for x in data if x >= 0]  # 最快速

# 字典解析
d = {x: randint(60, 100) for x in xrange(1, 21)}

{k: v for k, v in d.iteritems() if v > 90}

# 集合解析
s = set(data)
{x for x in s if x % 3 == 0}

# 元组
student = ('Jim', 16, 'male', 'jim@qq.com')
# 1. enum
NAME, AGE, SEX, EMAIL = xrange(4)
print
student[NAME]
# 2.
from collections import namedtuple

Student = namedtuuple('Student', ['name', 'age', 'sex', 'email'])
s2 = Student('Tom', 16, 'mail', 'tom@qq.com')
print
s2.name

# 统计列表的重复元素
li = [randint(0, 20) for _ in xrange(30)]
d = dict.fromkeys(li, 0)
# 1.
for x in li: d[x] += 1
# 2.
from collections import Counter

d2 = Counter(li)
d2.most_common(3)  # 重复数最高的三个元素

# 字典根据值value排序
sorted([3, 1, 5])  # 排序列表
(97, 'a') > (88, 'b')  # 元组的比较，每个元素从开始比较

d = {x: randint(60, 100) for x in 'abcde'}
# 1.
data = zip(d.itervalues(), d.iterkeys())
sorted(data)
# 2.
sorted(d.items(), key=lambda x: x[1])

# 多个字典中的公共键
sample('abcdefg', 3)
sample('abcdefg', randint(3, 6))  # 随机取出几个元素

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3.6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3.6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3.6))}

# 1.
# res = []
# for k in s1: if:
# k in s2 and k in s3: res.append(k)  # res.pop(k)

# 2. 使用集合
res = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

# 3.
m1 = map(dict.viewkeys, [s1, s2, s3])
res = reduce(lambda a, b: a & b, m1)

# 保持字典有序
d = {'Jim': (1, 35), 'Leo': (2, 38), 'Tom': (3, 44)}

from collections import OrderedDict

d = OrderedDict()  # 按进入字典的顺序打印
d['Jim'] = (1, 35)
d['Leo'] = (2, 38)
d['Tom'] = (3, 44)

from time import time

start = time()
raw_input()  # 等待输入
# ...
timesecond = time() - start

# 历史记录
# 1. 用队列存储
from collections import deque

q = deque([], 5)
q.append(1)  # 达到长度后，先进先出

li = list(q)  # 转换成列表类型

# 2. 将q存到文件中
import pickle

pickle.dump(q, open('test', 'w'))

q2 = pickle.load(open('test', 'r'))
