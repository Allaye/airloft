# import uuid
# from datetime import datetime, timezone, timedelta, date
# from django.db import models
# from django.utils.functional import cached_property
# # from account.models import User
# from utils.icao import ICAO
# # Create your models here.

# def generate_uuid():
#     '''
#     generate a unique id using uuid whenever a new aircraft is created
#     '''
#     return uuid.uuid4()

# def generate_icao(airport):
#     '''
#     generate a unique icao code whenever a new airport is created, 
#     that represent the airport, this code is going to be unique for 
#     each airport.
#     '''
#     return ICAO[airport]

# # print(generate_icao('ABE'))

# # Create your models here.
# class Aircraft(models.Model):
#     id = models.AutoField(primary_key=True)
#     serial_number = models.CharField(max_length=100, unique=True, default=generate_uuid)
#     manufacturer = models.CharField(blank=False, null=False, max_length=200)
#     model = models.TextField(blank=False, null=False, max_length=400, default="")
#     #technology = models.JSONField()
#     #members = models.ManyToManyField(User, related_name='all_members')
#     #start_date = models.DateField(default=date.today())
#     #end_date = models.DateField(blank=True, null=True)


#     # @property
#     # def is_completed(self):
#     #     """
#     #     check if the current project has been completed and closed
#     #     """
#     #     if self.end_date is None:
#     #         return False
#     #     return self.end_date < datetime.now().date()
    

#     # class Meta:
#     #     ordering = ['start_date']


# class Airport(models.Model):
#     id = models.AutoField(primary_key=True)
#     location = models.TextField(blank=False, null=False, max_length=400, default="")
#     name = models.CharField(blank=False, null=False, unique=True, max_length=200)
#     code = models.CharField(max_length=100, unique=True)


#     def save(self, *args, **kwargs):
#         """
#         Override the save method to generate a unique icao code
#         """
#         self.code = generate_icao(self.name)
#         super(Airport, self).save(*args, **kwargs)
#         # if self.code is None:
#         #     self.code = generate_icao(self.name)
#         # super().save(*args, **kwargs)


# class Flight(models.Model):
#     id = models.AutoField(primary_key=True)
#     description = models.TextField(blank=False, null=False, max_length=400, default="")
#     aircraft = models.ForeignKey(to=Aircraft, on_delete=models.CASCADE)
#     departure_airport = models.ForeignKey(to=Airport, related_name="depart", on_delete=models.CASCADE)
#     arrival_airport = models.ForeignKey(to=Airport, related_name="arrive", on_delete=models.CASCADE)
#     # user = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
#     departure_time = models.DateTimeField(auto_now_add=True)
#     arrival_time = models.DateTimeField(blank=True, null=True)
#     # activity_duration = models.DurationField(blank)


#     # def __str__(self):
#     #     """
#     #     convert to a string representation

#     #     Returns:
#     #         string: string representation of the object
#     #             " <title>  : <project> : <user> : <startdate>  : <enddate>"
#     #     """
#     #     if self.end_time is None:
#     #         return f"{self.description} : {self.project.title} : {self.user.username} : {self.start_time} : {'Activity in progress'}"
#     #     else:
#     #         return f"{self.description} : {self.project.title} : {self.user.username} : {self.start_time} : {self.end_time}"

    

#     # @property
#     # def is_running(self):
#     #     """
#     #     check if the activity is running

#     #     Returns:
#     #         bool: True if the activity is running, False otherwise
#     #     """
#     #     return self.end_time is None

#     # @cached_property
#     # def duration(self):
#     #     """
#     #     get the duration of the activity

#     #     Returns:
#     #         timedelta: duration of the activity
#     #     """
#     #     if self.is_running:
#     #         sec = datetime.now(timezone.utc) - self.start_time
#     #         return str(timedelta(seconds=round(sec.total_seconds())))
#     #     else:
#     #         sec = self.end_time - self.start_time
#     #         return str(timedelta(seconds=round(sec.total_seconds())))

