# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Color Captcha</title>
#     <link rel="stylesheet" type="text/css" href="main.css">
# </head>
# <body>
#     <div class="container">
#         <div class="color" style="background-color: #B6F56C" id="divColor"></div>
#         <form action="">
#             <input placeholder="Insert color" type="text" value=""/>
#             <button type="submit" onclick="sendColor()">Send</button>
#         </form>
#     </div>
# </body>
# <script src="main.js"></script>
# </html>
# нужно получить цвет и отправить через форму, цвет есть в коде и jwt токене
import time

import requests
import jwt

s = requests.session()

r = s.get("http://62.84.118.232:20002/?")
# print(r.text)
i = 0
while True:
    i = i+1
    print(i)
    d = jwt.decode(r.cookies.get("jwt"), algorithms="HS256", options={"verify_signature": False})
    r = s.post("http://62.84.118.232:20002/checkColor", json={"inputColor": d["color"]})
    print(r.text)
