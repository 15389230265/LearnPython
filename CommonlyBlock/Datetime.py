from datetime import datetime, timedelta, timezone


# datetime.now()返回当前日期和时间，其类型是datetime。
now = datetime.now()
print(now)

# 要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2015, 4, 19, 12, 30)
print(dt)

# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
print(dt.timestamp())
t = 233333333.0
print(datetime.fromtimestamp(t))
# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(t))
# datetime与str互转
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%a, %b %d %H:%M'))
# datetime加减
print(now + timedelta(hours=10))
# 本地时间转UTC时间本地时间是指系统设定时区的时间，
# 例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 创建时区UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))
# 强制设置为UTC+8:00
print(now.replace(tzinfo=tz_utc_8))
# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
print(utc_dt.astimezone(timezone(timedelta(hours=8))))
# astimezone()将转换时区为东京时间:
print(utc_dt.astimezone(timezone(timedelta(hours=9))))
