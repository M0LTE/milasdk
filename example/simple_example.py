"""
Client example.  Refreshes state every minute forever.
"""
import asyncio
import logging
import aiohttp

from credentials import USERNAME, PASSWORD
from milasdk import DefaultAsyncSession
from milasdk.api import MilaApi
from milasdk.gql import ApplianceSensorKind, SmartModeKind

_LOGGER = logging.getLogger(__name__)

async def update(api: MilaApi):
        r = await api.get_appliances()
        #r = await api.get_appliance("device here")
        #r = await api.get_appliance_sensor("device here", ApplianceSensorKind.Temperature)
        #r = await api.set_smart_mode("device here",SmartModeKind.ChildLock,True)
        print(r)
        r = await api.get_outdoor_data()
        print(r)

async def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)-8s %(message)s')

    #create the authenticated session
    async with DefaultAsyncSession(aiohttp.ClientSession(), USERNAME, PASSWORD) as session:
        api = MilaApi(session)

        while True:
            await update(api)
            await asyncio.sleep(60)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
