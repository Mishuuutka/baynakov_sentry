import sentry_sdk
from sentry_sdk import capture_exception, capture_message, configure_scope
sentry_sdk.init("https://eef2c57fe8ec432a8161b843519782eb@o402400.ingest.sentry.io/5263490")


with configure_scope() as scope:
    mas_scope = [0,0,0]
    scope.set_tag("Baynakov", "test")
    scope.set_tag("Lab", "6")
    scope.user = {'username' : 'Mishuuutka','id': 42, 'email': 'mishuuuutka@gmail.com'}
    try:
        print(mas_scope[4])
    except Exception:
        capture_message('ERROR')

mas = [1,2,3]

for i in range(len(mas)):
    print(mas[i+1])

zero = 1 / 0

inting = 1
stringing = 'string'
errorr = inting + stringing

