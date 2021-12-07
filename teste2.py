thisdict = {
  "brand": "auhsduifhaiufha\ndifhasi asuhfaiusdfisa\n asuidfhaiuasdfas\nFord",
  "model": "Mustang",
  "year": '1964'
}
for key, value in thisdict.items():
    print(key,value, '\n')
    if 'Ford' in value:
        a =1#print(key)
    else:
        print('none')
