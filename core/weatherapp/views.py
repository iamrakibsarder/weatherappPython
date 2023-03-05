from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup as bs
from requests import get


def weather_api(city):
    city = city.replace(' ', "+")
    url = f'https://www.google.com/search?q=weather+of+{city}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'cookie': '__Secure-ENID=4.SE=R-4oRzwc1ptDfLj01zbEIe56B27vS46eWR12S2tV4lNaJTpfUeyND-6LhAYKuUOP_xmOXB1h7_AEI7uUcKmXUJfbJwlNS0_mv61qXeXjHiHZX2XV7fYRjPsSgJHtx2i36mBGtGna7mBbv42elkmFORCNuGu5J9IOyeEmLuFd7d_mI2XNn_cw1SmQmaP4ad6hyfB_44WLwiD2k6157JQPg849OiXmJhw4u-uy1vbMj3FQjZnAnby3PonWtw; SEARCH_SAMESITE=CgQI8ZYB; SID=SQi_7rq0YhgxrtjuiRZTuvFvupJ6nyJc0rSswz_9mcgKynD29LKAT8ON_NuLhACaTvWNoA.; __Secure-1PSID=SQi_7rq0YhgxrtjuiRZTuvFvupJ6nyJc0rSswz_9mcgKynD25D7OGp-AbZay0X2aeXwphw.; __Secure-3PSID=SQi_7rq0YhgxrtjuiRZTuvFvupJ6nyJc0rSswz_9mcgKynD2WMIZH9Aa9kebjD7a-K58Jg.; HSID=A5dIPR2glP1uGuRb3; SSID=Az1LOMyISsJtx-LE3; APISID=IR5Ix98E_10rp23O/AWF-4__vEgbOQanA9; SAPISID=TbZN9joK9eMBSOi1/APMUO4Myv31ZPFDX0; __Secure-1PAPISID=TbZN9joK9eMBSOi1/APMUO4Myv31ZPFDX0; __Secure-3PAPISID=TbZN9joK9eMBSOi1/APMUO4Myv31ZPFDX0; OTZ=6867872_32_32__32_; AEC=ARSKqsKESBuIchqbeAcYuX8eyeI1O1mIV8glsmzk2laBosGls8cQFHZxQQ; NID=511=TiaZpZ3h2aT-CshIpQS9J8G2CzzBcnx9IcRwsDOWVDpzjmIrmns9ZeJV__jlqeWxGOCDyei7gBLraLRxtXiL1duDHTXbv1gKTj3nU1XEI4zeMOvbpy0z2yjwa1jA3KYtGEGZkehVGhcCUWbcwD9oq53ODzacesWnGmkj8jeYNlAu5CB0s0DBNk5wRary3_umMJLAfQGzKu8AnU_XGVDAaW7B4_luw8fpSpF4fiXRB-EbV2larZpAA3PPd1GGxH6B3vEleLslxfaYDNG29UF0cHI63W6tAOycaJSZMNJxpY6g1DTWKFaXpBGC9JfznhJTTLEbcimwfKPv-oF0BkfvgV92-aiKuK1ZCxP15ETZUvah9joDZuH_ccWu1DFvsMpoA0Xdrh8D0cQuBypTYfE; DV=4yPCn5t3O3NbwEtSPKiaEkqqSwmdX1iXimc7DQWIBQEAAEBL1W1MikEpVgAAADxm4ZwXIJaBLwAAAHjU1yhfGuRCEQAAAA; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjc0OTMzNDc3MDc1MDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDIzNzk4MzQ0OAogIGxvbmdpdHVkZV9lNzogOTA0NDA0NjMwCn0KcmFkaXVzOiAyMjgxNDE0LjMzMjQ2Njg4MTMKcHJvdmVuYW5jZTogNgo=; 1P_JAR=2023-01-28-19; SIDCC=AFvIBn-M5XYISy2e8a0DgrvFH7mKmleJ2ogsnlCQ02K9h3pw6_-JoecwobcPmbcb69pN71rWmpY; __Secure-1PSIDCC=AFvIBn-U06TBDdyDh_zw-jc8-rUJIWX7j-MpciHQFakLu2_lNm7aMEUtH2TU3lDbxsFuo8CRHnyD; __Secure-3PSIDCC=AFvIBn9xVWbRlUwPVosKT8wJ6qSLCzNhBVfQaQqYvR4QyFPh9zmcWoWnDdyVOECuXEXEJd29oh4'
    }
    res = get(url, headers=headers)
    soup = bs(res.text, 'html.parser')

    result = {"temp": soup.find('span', {"id": "wob_tm"}).text, "weather": soup.find('span', {"id": "wob_dc"}).text,
              "city_name": soup.find('span', {"class": "BBwThe"}).text,
              "day": soup.find('div', {"class": "wob_dts"}).text}

    return result


def django(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        result = weather_api(city)
        context = {'result': result}
    else:
        context = {}
    return render(request, 'weatherapp/home.html',context)