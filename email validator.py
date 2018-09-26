##Email Validator - enter an email address...check to see if it is valid/correct
import dns.resolver
errorone = False
errortwo = False
correct = 0
allowed = set('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm."(),:;<>@[\]')
email = input("Please enter your email address: ")
while True:
    if set(email).issubset(allowed):
        correct += 1
    else:
        errorone = True
    try:
        splitted = email.split('@',1)[1]
        query = dns.resolver.query(splitted,'MX')
    except:
        errortwo = True
        break
    else:
        correct += 1
        break
while True:
    if correct == 2:
        print("Valid email address given!")
        break
    else:
        if errorone == True:
            print()
            print('Failed check one: Invalid Characters')
        if errortwo == True:
            print()
            print('Failed check two: DNS Query. Forgot the @ symbol? Check your domain?')
            print()
            print("Invalid email address!")
            print()
            break
