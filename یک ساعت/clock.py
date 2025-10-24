m_hour, m_minute = map(int, input().split())
hour = (12 - m_hour) % 12
minute = (60 - m_minute) % 60
print("%.2d:%.2d" % (hour, minute))