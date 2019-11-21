from django.db import models

class UserInfo(models.Model):
    ip_address = models.CharField(max_length=100, default="None")
    age = models.CharField(max_length=100, default="None")
    gender = models.CharField(max_length=100, default="None")
    education = models.CharField(max_length=100, default="None")
    mturkId = models.CharField(max_length=100)
    userResponses = models.CharField(max_length=50)
    def __str__(self):
        return self.mturkId

'''
class Algorithm(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Query(models.Model):
    # the name of the query (i.e. 'women's world cup')
    query_name = models.CharField(max_length=100)
    def __str__(self):
        return self.query_name

class Response(models.Model):
    respondent = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    chosen_alg = models.ForeignKey(Algorithm, on_delete=models.CASCADE, related_name="chosen")
    unchosen_alg = models.ForeignKey(Algorithm, on_delete=models.CASCADE, related_name="unchosen")
    # if we want to store more accurate time data, change this
    time_elapsed = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Query: " + self.query.query_name + "Choice: " + self.chosen_alg.name
'''
