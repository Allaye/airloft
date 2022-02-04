import uuid
from datetime import datetime, timedelta, tzinfo
from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from django.utils.functional import cached_property

# from account.models import User
from utils.icao import ICAO

# Create your models here.


def generate_uuid():
    """
    generate a unique id using uuid whenever a new aircraft is created
    """
    return uuid.uuid4()


def generate_icao(airport):
    """
    generate a unique icao code whenever a new airport is created,
    that represent the airport, this code is going to be unique for
    each airport.
    """
    return ICAO[airport]


def validate_future_flight(date):
    """
    validate if the datetime is in the future, meaning at least one day
    from the date it was created.
    """
    now = datetime.now().replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
    print(date.replace(tzinfo=None)+ timedelta(minutes=33))
    print(datetime.fromisoformat(now))
    if date.replace(tzinfo=None) > datetime.fromisoformat(now) + timedelta(days=1):
        return True
    else:
        raise ValidationError("you can only create a flight form 24 hours into the future")


# print(generate_icao('ABE'))
class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ""

# Create your models here.
class Aircraft(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, unique=True, default=generate_uuid)
    manufacturer = models.CharField(blank=False, null=False, max_length=200)
    model = models.TextField(blank=False, null=False, max_length=400, default="")
    # technology = models.JSONField()
    # members = models.ManyToManyField(User, related_name='all_members')
    # start_date = models.DateField(default=date.today())
    # end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
    # @property
    # def is_completed(self):
    #     """
    #     check if the current project has been completed and closed
    #     """
    #     if self.end_date is None:
    #         return False
    #     return self.end_date < datetime.now().date()

    # class Meta:
    #     ordering = ['start_date']


class Airport(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.TextField(blank=False, null=False, max_length=400, default="")
    name = models.CharField(blank=False, null=False, unique=True, max_length=200)
    code = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a unique icao code
        """
        self.code = generate_icao(self.name)
        super(Airport, self).save(*args, **kwargs)
        # if self.code is None:
        #     self.code = generate_icao(self.name)
        # super().save(*args, **kwargs)


class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=False, null=False, max_length=400, default="")
    aircraft = models.ForeignKey(to=Aircraft, blank=True, null=True, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(to=Airport, blank=True, null=True, related_name="depart", on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(to=Airport, blank=True, null=True, related_name="arrive", on_delete=models.CASCADE)
    # user = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(validators=[validate_future_flight])
    arrival_time = models.DateTimeField(blank=False, null=False)
    # activity_duration = models.DurationField(blank)

    def clean(self) -> None:
        if self.arrival_time is None:
            raise ValidationError("arrival time is required")
        departure = self.departure_time.replace(tzinfo=None)
        arrive = self.arrival_time.replace(tzinfo=None)
        if arrive - departure < timedelta(minutes=30):
            raise ValidationError("arrival time must be at least 30 minutes after departure time")
        return super().clean()

    def save(self, *args, **kwargs):
        """
        class the overridden clean method to validate the flight arrival time
        """
        self.full_clean()
        super(Flight, self).save(*args, **kwargs)
        
    # def __str__(self):
    #     """
    #     convert to a string representation

    #     Returns:
    #         string: string representation of the object
    #             " <title>  : <project> : <user> : <startdate>  : <enddate>"
    #     """
    #     if self.end_time is None:
    #         return f"{self.description} : {self.project.title} : {self.user.username} : {self.start_time} : {'Activity in progress'}"
    #     else:
    #         return f"{self.description} : {self.project.title} : {self.user.username} : {self.start_time} : {self.end_time}"

    # @property
    # def is_running(self):
    #     """
    #     check if the activity is running

    #     Returns:
    #         bool: True if the activity is running, False otherwise
    #     """
    #     return self.end_time is None

    # @cached_property
    # def duration(self):
    #     """
    #     get the duration of the activity

    #     Returns:
    #         timedelta: duration of the activity
    #     """
    #     if self.is_running:
    #         sec = datetime.now(timezone.utc) - self.start_time
    #         return str(timedelta(seconds=round(sec.total_seconds())))
    #     else:
    #         sec = self.end_time - self.start_time
    #         return str(timedelta(seconds=round(sec.total_seconds())))
