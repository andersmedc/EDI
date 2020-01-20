import base64
#ændre filnavnet for input
with open("anders.tiff", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
image_result = open('base64.txt', 'wb')
# create a writable image and write the decoding result 
image_result.write(my_string)
print(my_string.decode('utf-8'))