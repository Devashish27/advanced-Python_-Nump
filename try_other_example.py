try:
    print("I will throw an exception if there's any problem..!!")
except Exception as e:
    print("I will run only if try block fails...!!")
else:
    print("I will run only if there's no exception. Use This To RUn Code which should"
          "only execute if there's no exception")
finally:
    print("This Will Be Printed In Every Case..!!")
    