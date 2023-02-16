def func(d):
      if key in d.keys():
            return "Key is present"
      else:
            return "Key isn't present"
d={'A':1,'B':2,'C':3}
key=input("Enter key to check:")
print(func(d))
