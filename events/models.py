from django.db import models

class Event(models.Model):
    invoker = models.CharField(max_length=255) # The user who triggered an event.
    action = models.CharField(max_length=255) # The action the user tried to preform.
    response = models.IntegerField() # The response given by the server.
    ip = models.IPAddressField() # The IP of the invoker.
    additional = models.CharField(max_length=255) # Additional information (optional).
