import requests
import cv2
import pytesseract
from bs4 import BeautifulSoup
import urllib.request
import time

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# you can adjust the blurs used and their strengths until your OCR starts reading text accurately
def denoise_ToText(img):
    image = cv2.imread(img)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    median_blurred = cv2.medianBlur(gray_image, 5)
    gaussian_blurred = cv2.GaussianBlur(median_blurred, (5, 5), 0)
    bilateral_filtered = cv2.bilateralFilter(gaussian_blurred, d=9, sigmaColor=75, sigmaSpace=75)

    cv2.imwrite('./solve/denoised_image.png', bilateral_filtered)

    text = pytesseract.image_to_string('./solve/denoised_image.png')
    print (text)
    return text

def solve_equation(eqn):
    # Solve the equation based on the operator
    # ADD SUB MUL MOD POW
    equation = eqn.split(" ")
    # print(equation)
    a = equation[0]
    b = equation[2]
    operator = equation[1]
    if operator == "ADD":
        return int(a) + int(b)
    elif operator == "SUB":
        return int(a) - int(b)
    elif operator == "MUL":
        return int(a) * int(b)
    elif operator == "MOD":
        return int(a) % int(b)
    elif operator == "POW":
        return int(a) ** int(b)
    else:
        return 0


for i in range (49):
    URL = "http://127.0.0.1:5000/"
    if i == 0:
        r = requests.get(URL)
        htmldata = r.text
        cookies = r.cookies
    else:
        htmldata = x.text
        cookies = x.cookies

    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img'):
        equation = item['src']
        equation_add = "http://127.0.0.1:5000/" + equation

    urllib.request.urlretrieve(equation_add, "./solve/equation.png")

    equation_text = denoise_ToText('./solve/equation.png')
    answer = solve_equation(equation_text)
    x = requests.post(URL + "answer", data = {'answer': answer}, cookies = cookies)
    #time.sleep(0.5)

    print("ANSWER:",answer)
    soup = BeautifulSoup(x.text, 'html.parser')
    score = soup.find('p').get_text()
    print(score)
    print(x.text)
    


