# 场景：踢猫效应

# 自然语言描述：小孩很气愤，就用左脚踢了身边的猫
# 提取关键词：左脚 踢 猫 => 左 踢 猫
# 调整语序：踢 猫 左

# 定义函数：
def 踢(猫, 左):
    # 根据函数签名，还原自然语言描述
    # kick the cat with left foot
    print(f"用{左}脚踢了{猫}")

# 调用函数：
踢('加菲猫', '左')
踢('波斯猫', '右')

# 古灵精怪：
踢('狗', '中')
踢(12, 3.0)

# 发现问题，引出“类型”概念，
# 但 Python 无法直接解决此问题
