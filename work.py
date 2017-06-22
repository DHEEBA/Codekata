def Workingday(s):
    if (s.lower()=="sunday")or(s.lower()=="saturday"):
        return False
    else:
        return True
q=input("Enter any day")
x=Workingday(q)
print(x)
