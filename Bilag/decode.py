import base64 
#ændre filnavnet for input
image = open('base64.txt', 'rb') 
image_read = image.read() 
image_64_decode = base64.decodestring(image_read) 
#ændre filnavnet for output
image_result = open('outputfil.tiff', 'wb')
# create a writable image and write the decoding result 
image_result.write(image_64_decode)