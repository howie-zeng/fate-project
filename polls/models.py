from django.db import models

'''
For more field information, check: https://docs.djangoproject.com/en/2.2/ref/models/fields/
'''


# ['age','gender','education level','ip address', 'browser-info', 'mturk-id']
class UserInfo(models.Model):
    mturk_id = models.CharField(max_length=50, default="None", primary_key=True)
    ip_address = models.CharField(max_length=50, default="0.0.0.0")
    browser_info = models.CharField(max_length=50, default="None")
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    education = models.CharField(max_length=50)

    # will set the timezone.now() only when the instance is created,
    date_submitted = models.DateTimeField(auto_now_add=True)

    # For debugging purposes
    def __str__(self):
            return "ID: " + self.mturk_id + ", Age: " + self.age + ", gender: " + self.gender + \
                   ", Education: " + self.education + ", IP: " + self.ip_address + ", Browser: " + self.browser_info


# ['mturk-id','algorithm','query','rating','time spent']
class Response(models.Model):
    mturk_id = models.CharField(max_length=50, default="None")
    algorithm = models.CharField(max_length=10)
    query = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
    time_spent = models.PositiveSmallIntegerField()

    # For debugging purposes
    def __str__(self):
        return "ID: " + self.mturk_id + ", Algorithm: " + self.algorithm + ", Query: " + self.query + \
               ", rating: " + self.rating.__str__() + ", timeSpent: " + self.time_spent.__str__()
