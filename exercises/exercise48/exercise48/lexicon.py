directions = ["north","south","east","west"]
verbs = ["go","kill","eat"]
stops = ["the","in","of"]
nouns = ["bear","princess"]

def scan(input):
  words = input.split()
  tuples = []
  for value in words:
    tuples.append((get_type(value), get_value(value)))
  return tuples

def get_type(input):
  if input in directions: return "direction"
  elif input in verbs:    return "verb"
  elif input in stops:    return "stop"
  elif input in nouns:    return "noun"
  elif is_number(input):  return "number"
  else:                   return "error"

def get_value(input):
  converted_number = convert_number(input)
  if converted_number != None:
    return converted_number
  else:
    return input

def is_number(input):
  return convert_number(input) != None

def convert_number(input):
  try:
    return int(input)
  except ValueError:
    return None
