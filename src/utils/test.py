from datetime import datetime

# 获取两个时间点
time1 = datetime.now()
time2 = datetime(2023, 12, 31, 23, 59, 59)  # 示例时间点

# 转换为时间戳
timestamp1 = int(time1.timestamp())
timestamp2 = int(time2.timestamp())

# 计算时间差（秒）
time_difference = timestamp2 - timestamp1

print("两个时间点之间的差（秒）:", time_difference)