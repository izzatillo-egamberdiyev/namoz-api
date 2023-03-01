import aiohttp
import asyncio

from urllib.request import urlopen
from bs4 import BeautifulSoup

async def ParsingNamoz(shaxar):

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://namozvaqti.uz/shahar/{shaxar}') as response:
            soup = BeautifulSoup(await response.text(), features="lxml")

            vaqt = soup.find('h5', class_='vil').text
            vaqt = vaqt.replace('\n', '')
            vaqt = vaqt.replace('   ', '')
            bomdod = soup.find('p', id="bomdod").text
            quyosh = soup.find('p', id="quyosh").text
            peshin = soup.find('p', id="peshin").text
            asr = soup.find('p', id="asr").text
            shom = soup.find('p', id="shom").text
            xufton = soup.find('p', id="hufton").text

            result ={
                'vaqt' : vaqt,
                'bomdod' : bomdod,
                'quyosh' : quyosh,
                'peshin' : peshin,
                'asr' : asr,
                'shom' : shom,
                'xufton' : xufton,
            }
    return result

async def test():
    r = await ParsingNamoz('toshkent')
    print(r)


            # print("Status:", response.status)
            # print(bomdod)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())