
from random import randrange, random
from time import time, sleep
from threading import Thread
from bots.base.base import BaseFarmer
from bots.base.utils import to_localtz_timestamp, api_response
from .strings import HEADERS, URL_DRIVE, URL_INFO, URL_INIT, MSG_BALANCE


class BotFarmer(BaseFarmer):
    name = "racememe_bot"
    extra_code = "r_102796269"
    init_data = None
    riding_thread = None
    debug = False
    initialization_data = dict(peer=name, bot=name, url=URL_INIT)

    def set_headers(self, *args, **kwargs):
        self.headers = HEADERS.copy()
        self.get = api_response(super().get)
        self.post = api_response(super().post)

    def authenticate(self, *args, **kwargs):
        auth_data = self.initiator.get_auth_data(**self.initialization_data)
        self.init_data = auth_data['url'].split('tgWebAppData=')[-1].split('&')[0]

    def refresh_token(self):
        self.initiator.connect()
        self.authenticate()
        self.initiator.disconnect()

    @property
    def ready_to_ride(self):
        self.sync()
        traffic_light = self.info['user']['trafficLight']
        return traffic_light['trafficLightState'] == 'green' and traffic_light['remainingTime'] > 1500

    @property
    def fuel(self):
        return self.info['user']['fuel']['lastFuelAmount']

    def set_start_time(self):
        self.start_time = time() + 3600

    def ride(self):
        self.sync()
        if not self.ready_to_ride:
            return
        liters = round(randrange(0, 3) + random(), 1)
        if liters <= self.fuel:
            meters = liters * 100 - randrange(0, 6)
            payload = {"numberOfMeters": meters, "numberOfLiters": liters}
            response = self.post(URL_DRIVE.format(init_data=self.init_data), json=payload)

    def ride_in_thread(self):
        for _ in range(1000):
            self.ride()
            sleep(3)

    def start_riding_thread(self):
        if not self.riding_thread or not self.riding_thread.is_alive():
            self.riding_thread = Thread(target=self.ride_in_thread)
            self.riding_thread.start()

    def sync(self):
        response = self.get(URL_INFO.format(init_data=self.init_data))
        if response:
            self.info = response

    def farm(self):
        self.start_riding_thread()
        self.sync()
        self.log(MSG_BALANCE.format(meters=self.info['user']['distance']['lastDistanceAmount']))
        pass
