

import base64

with open("app/static/css/img/3. Bellezas del Estado Bolivar Canaima.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

print(encoded_string)
