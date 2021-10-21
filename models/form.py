from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase
from database import db



class Form(BaseModel):
    Name = pw.CharField()
    Gender = pw.CharField(unique=False)
    Birthdate = pw.DateTimeField()
    Address = pw.CharField(null=True)
    Medications = pw.CharField(null=True)
    Nameofnextkin = pw.CharField(null=True)
    Phoneofnextkin = pw.CharField(null=True)
    Reasonforvisit = pw.CharField(null=True)
    Fever = pw.BooleanField(null=True, default=False)
    Headache = pw.BooleanField(null=True, default=False)
    Nightchills = pw.BooleanField(null=True, default=False)
    Sorethroat = pw.BooleanField(null=True, default=False)
    Cough = pw.BooleanField(null=True, default=False)
    Breathingdiff = pw.BooleanField(null=True, default=False)
    Diarrhoea = pw.BooleanField(null=True, default=False)
    Chestpain = pw.BooleanField(null=True, default=False)
    Legnumbness = pw.BooleanField(null=True, default=False)
    Handnumbness = pw.BooleanField(null=True, default=False)
    Facenumbness = pw.BooleanField(null=True, default=False)
    Diabetes = pw.BooleanField(null=True, default=False)
    Highbloodpressure = pw.BooleanField(null=True, default=False)
    Highcholesterol = pw.BooleanField(null=True, default=False)
    Asthma = pw.BooleanField(null=True, default=False)
    Kidneydisease = pw.BooleanField(null=True, default=False)
    Arthritis = pw.BooleanField(null=True, default=False)
    Pancreaticcancer = pw.BooleanField(null=True, default=False)
    Livercancer = pw.BooleanField(null=True, default=False)
    Colorectalcancer = pw.BooleanField(null=True, default=False)
    COPD = pw.BooleanField(null=True, default=False)
    Depression = pw.BooleanField(null=True, default=False)
    Lungcancer = pw.BooleanField(null=True, default=False)
