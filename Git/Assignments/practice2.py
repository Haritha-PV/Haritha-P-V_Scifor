#ASSIGNMENT ON GIT(30-06-2024)

#Create a function which takes in an encoded string 
# and returns a dictionary according to the following example:


encoded_string='John000Doe000123'
def encoded_string_dict(encoded_string):
  data=encoded_string.split('0')
  for i in range(data.count('')):
    data.remove('')

  dict_data={"first_name":str(data[0]),"last_name":str(data[1]),"id":str(data[2])}
  return dict_data
encoded_string_dict(encoded_string)