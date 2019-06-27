from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.utils.timezone import utc
import datetime
import math

class PinDrop(models.Model):
	pinuser = models.ForeignKey(User,related_name='userpin', on_delete=models.CASCADE)
	pinphoto = models.ImageField(upload_to='media/',blank=True, null=True)
	pindate = models.DateTimeField(auto_now_add=True)
	pinvisiteddate = models.DateTimeField(auto_now_add=True)
	pinbody = models.TextField()
	pinlocation = models.PointField(srid=4326)

	def pintimeago(self):
	    if self.pindate:
	        now = datetime.datetime.utcnow().replace(tzinfo=utc)
	        timediff = now - self.pindate
	        return math.floor(timediff.total_seconds()/60)

	def pinhours(self):
		if self.pindate:
			now = datetime.datetime.utcnow().replace(tzinfo=utc)
			timediff = now - self.pindate
			return math.floor(timediff.total_seconds()/3600)

	def pindays(self):
		if self.pindate:
			now = datetime.datetime.utcnow().replace(tzinfo=utc)
			timediff = now - self.pindate
			return math.floor(timediff.total_seconds()/86400)

	def shortpindate(self):
		return self.pindate.strftime('%e %b %Y')

	def shortvisitdate(self):
		return self.pinvisiteddate.strftime('%e %b %Y')

	def getUsername(self):
		return self.pinuser.username

	def pinsummary(self):
		return self.pinbody[:100]

	def longitude(self):
		return self.pinlocation.x

	def latitude(self):
		return self.pinlocation.y


class Countries(models.Model):
    country_type = models.CharField(max_length=17)
    name = models.CharField(max_length=36)
    abbrev = models.CharField(max_length=13)
    formal_name = models.CharField(max_length=52)
    pop_est = models.BigIntegerField()
    gdp_md_est = models.FloatField()
    pop_year = models.IntegerField()
    lastcensus = models.IntegerField()
    gdp_year = models.IntegerField()
    continent = models.CharField(max_length=23)
    region_un = models.CharField(max_length=23)
    region_wb = models.CharField(max_length=26)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ["name","geom"]
