# coding= UTF-8
# هذا البرنامج يقوم بفتح الباب

def getPasswordFromMic():
    return 'أفتح الباب يا باب'


def getPassword():
    return 'أفتح الباب يا باب'


def openDoor():
    return 'تفضل، أغلاق الباب خلفك إذا سمحت'


print('مرحبا بك أنا الباب')
print('ما هي كلمة السر؟')


password = getPasswordFromMic()

while password != getPassword():
	Password = getPasswordFromMic()

print(openDoor())
