def verbing(s):
  if len(s) >= 3:
    if s[-3:] == "ing":
      s += "ly"
    else:
      s += "ing"
    return s
  else:
    return s 