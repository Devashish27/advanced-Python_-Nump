try:
    file = open("this.txt", 'r')
except EOFError as e:
    print("eof error")
except IOError as e:
    print("We Can Handle This Error..!!")
finally:
    print("This Will Be Printed Irrespective Of Exception Occurrence")
