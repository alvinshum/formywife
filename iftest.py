rain = input('請問有沒有下雨：')
if rain == '有':
    print('小心地滑')
    print('努力')
    breakfast = input('今天吃了早餐嗎：')
    if breakfast == '有':
       print('那就好了')
    if breakfast == '沒有':
       print('不吃早餐沒帶力氣了！')   
if rain == '沒有':
    print('注意天氣')
    print('今天也要加油')