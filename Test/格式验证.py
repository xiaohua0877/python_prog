###直接使用快捷键 Ctrl+Alt+L 可以批量格式化代码，不用全选。
import random

# 生成随机浮点数
float1 = random.uniform(10, 20)
float2 = random.uniform(1, 3)
# 生成随机整数[a,b]之间，闭区间
int1 = random.randint(10, 20)
int2 = random.randint(1, 3)
# 随机字符
str1 = random.choice('abcdefg')
# 随机字符串
str3 = random.choice(['apple', 'pear', 'peach', 'orange', 'lemon'])
# 随机打乱#洗牌
items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
