
# id, name, zipcode, avg_price, year of practice

# sort by avg_price

def flaotify(str):
  try:
    return float(str)
  except ValueError:
    return str
  
def sort_doctor(csv_string):
  doctors = map(lambda x: x.split(','), csv_string.split('\n'))
  for d in doctors:
    d[3] = float(d[3])
  doctors.sort(key= lambda d: d[3])
  return doctors.pop


  
csv = '''1,bob,94352,35.23,23
2,alice,98463,453.2,10
3,jack,94736,14.45,9'''

print sort_doctor(csv)