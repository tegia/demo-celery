import uuid
from datetime import datetime
from locust import HttpUser, TaskSet, task, between
import random
from random import randint

# class MetricsTaskSet(TaskSet):
#     _deviceid = None

#     def on_start(self):
#         self._deviceid = str(uuid.uuid4())

#     @task(1)
#     def testpost(self):
#         # self.client.post('/api/v1/service/search?category=1,1,1&from=0&size=50')
#         # self.client.post('/api/v1/service/search?price_from=300&price_to=400&category=1,1,1&from=0&size=100')
#         # self.client.post('/api/v1/service/search?price_from=50&price_to=400&category=1,1,1&date_from=2020-07-01&date_to=2020-07-20&full_text_search=Akademeia&from=0&size=100&ages=9,10&hour_from=01:00:00&hour_to=02:00:00&exact_days=sobota,środa&service_type_id=1')
#         # self.client.post('/api/v1/service/search?price_from=50&price_to=400&category=1,1,1&date_from=2020-07-01&date_to=2020-07-20&full_text_search=Akademeia&from=0&size=100&ages=9,10&hour_from=01:00:00&hour_to=02:00:00&exact_days=sobota,środa&service_type_id=1')
#         self.client.post('/api/v1/service/search?price_from=50&price_to=400&category=3,14,202&date_from=2020-07-01&date_to=2020-07-20&full_text_search=Academy&from=0&size=100&ages=9,10&hour_from=17:00:00&hour_to=19:00:00&exact_days=sobota,środa')


# class MetricsLocust(User):
#     task_set = MetricsTaskSet
#     wait_time = between(1, 3)

class MetricsLocust(HttpUser):
    @task
    def testpost(self):
        # self.client.post('/api/v1/service/search?category=1,1,1&from=0&size=50')
        # self.client.post('/api/v1/service/search?price_from=300&price_to=400&category=1,1,1&from=0&size=100')
        # self.client.post('/api/v1/service/search?price_from=50&price_to=400&category=1,1,1&date_from=2020-07-01&date_to=2020-07-20&full_text_search=Akademeia&from=0&size=100&ages=9,10&hour_from=01:00:00&hour_to=02:00:00&exact_days=sobota,środa&service_type_id=1')
        # self.client.post('/api/v1/service/search?price_from=50&price_to=400&category=1,1,1&date_from=2020-07-01&date_to=2020-07-20&full_text_search=Akademeia&from=0&size=100&ages=9,10&hour_from=01:00:00&hour_to=02:00:00&exact_days=sobota,środa&service_type_id=1')
        #self.client.post('/api/v1/service/search?price_from=50&price_to=400&category=3,14,202&date_from=2020-07-01&date_to=2020-07-20&full_text_search=Academy&from=0&size=100&ages=9,10&hour_from=17:00:00&hour_to=19:00:00&exact_days=sobota,środa')
        # self.client.post('/api/v1/service/search?price_from=99&price_to=624&category=1,3,6&date_from=2020-07-01&date_to=2020-07-08&full_text_search=Eight green dogs evaluated&from=0&size=100&ages=2,8&hour_from=01:00:00&hour_to=14:00:00&exact_days=sobota,niedziela')
        # words = [["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "ThirdTeen", "FourTeen"],
        #     ["red", "yellow", "green", "AliceBlue", "AntiqueWhite", "Aqua",
        #     "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue"],
        #     ["cats", "dogs", "zebras", "lion", "tiger", "elephant", "Aves", "Bovinae", "Canidae", "Equidae",
        #     "Leporidae", "Osteichthyes", "Aardvark", "Albatross", "Alligator", "Alpaca", "Bee", "Camel"],
        #     ["jumped.", "danced.", "wrote poetry.", "assessed", "evaluated", "transmitted", "commissioned"]]

        # start_date_arr = ["2020-07-01", "2020-07-02", "2020-07-03", "2020-07-04"]
        # end_date_arr = ["2020-07-05", "2020-07-06", "2020-07-07", "2020-07-08", "2020-07-09", "2020-07-10"]
        # start_time_arr = ["01:00:00", "01:10:00", "01:20:00", "01:30:00", "02:00:00", "02:10:00", "02:20:00", "02:30:00", "03:10:00", "03:20:00"]
        # end_time_arr = ["10:00:00", "11:10:00", "12:20:00", "13:30:00", "14:00:00", "15:10:00", "16:20:00", "17:30:00", "18:10:00", "19:20:00"]
        # exact_day_arr = ["wtorek", "piątek", "niedziela", "sobota"]
        # # self.client.post('/api/v1/service/search?price_from=50&price_to=900&category=8,6,8&date_from=2020-07-01&date_to=2020-07-20&full_text_search=CornflowerBlue&from=0&size=100&ages=3,4&hour_from=02:00:00&hour_to=19:00:00&exact_days=sobota,niedziela')
        # url = '/api/v1/service/search?'
        # url = url + "price_from=" + str(randint(50, 400)) + "&price_to=" + str(randint(401, 900)) + "&category=" + str(randint(1, 10)) + "," + str(randint(1, 10)) + "," + str(randint(1,
        #                                                                                                                                                        10)) + "&date_from=" + random.choice(start_date_arr) + "&date_to=" + random.choice(end_date_arr) + "&full_text_search=" + ' '.join([random.choice(a) for a in words]) + "&from=0&size=100" + "&ages=" + str(randint(1, 3)) + "," + str(randint(4, 10)) + "&hour_from=" + random.choice(start_time_arr) + "&hour_to=" + random.choice(end_time_arr) + "&exact_days=" + random.choice(exact_day_arr) + "," + random.choice(exact_day_arr)
        # # url = url + "price_from=" + str(randint(50, 400)) + "&price_to=" + str(randint(401, 900)) + "&category=" + str(randint(1, 10)) + "," + str(randint(1, 10)) + "," + str(randint(1,
        # #                                                                                                                                                        10)) + "&date_from=" + random.choice(start_date_arr) + "&date_to=" + random.choice(end_date_arr) + "&from=0&size=100" + "&ages=" + str(randint(1, 3)) + "," + str(randint(4, 10)) + "&hour_from=" + random.choice(start_time_arr) + "&hour_to=" + random.choice(end_time_arr) + "&exact_days=" + random.choice(exact_day_arr) + "," + random.choice(exact_day_arr)
        # self.client.post(url)
        
        self.client.get('/add/'+str(randint(1, 30))+'/'+str(randint(31, 60))+'/'+ str(uuid.uuid4()))
    wait_time = between(1, 3)