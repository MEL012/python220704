# DemoDict.py
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(len(device))
device["아이폰"] = 6
print(device["아이폰"])
device["맥북"] = 15
print(device)
del device["아이패드"]
print(device)

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

device2 = device
print(device2)
device2["윈도우"] = 30
print(device)
print(device2)
print(id(device))
print(id(device2))


isRight = True
print(type(isRight))
print(1 < 2)
print( 1 != 2)
print(1 == 2)
