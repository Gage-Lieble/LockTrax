from django.db import models

# Create your models here.


STATES = (
        ('Chose a State', 'Chose a state'),
        ('Alabama','Alabama'),
        ('Alaska','Alaska'),
        ('Arizona','Arizona'),
        ('Arkansas','Arkansas'),
        ('California','California'),
        ('Colorado','Colorado'),
        ('Connecticut','Connecticut'),
        ('Delaware','Delaware'),
        ('Florida','Florida'),
        ('Georgia','Georgia'),
        ('Guam','Guam'),
        ('Hawaii','Hawaii'),
        ('Idaho','Idaho'),
        ('Illinois','Illinois'),
        ('Indiana','Indiana'),
        ('Iowa','Iowa'),
        ('Kansas','Kansas'),
        ('Kentucky','Kentucky'),
        ('Louisiana','Louisiana'),
        ('Maine','Maine'),
        ('Maryland','Maryland'),
        ('Massachusetts','Massachusetts'),
        ('Michigan','Michigan'),
        ('Minnesota','Minnesota'),
        ('Mississippi','Mississippi'),
        ('Missouri','Missouri'),
        ('Montana','Montana'),
        ('Nebraska','Nebraska'),
        ('Nevada','Nevada'),
        ('New Hampshire','New Hampshire'),
        ('New Jersey','New Jersey'),
        ('New Mexico','New Mexico'),
        ('New York','New York'),
        ('North Carolina','North Carolina'),
        ('North Dakota','North Dakota'),
        ('Ohio','Ohio'),
        ('Oklahoma','Oklahoma'),
        ('Oregon','Oregon'),
        ('Pennsylvania','Pennsylvania'),
        ('Rhode Island','Rhode Island'),
        ('South Carolina','South Carolina'),
        ('South Dakota','South Dakota'),
        ('Tennessee','Tennessee'),
        ('Texas','Texas'),
        ('Utah','Utah'),
        ('Vermont','Vermont'),
        ('Virginia','Virginia'),
        ('Washington','Washington'),
        ('West Virginia','West Virginia'),
        ('Wisconsin','Wisconsin'),
        ('Wyoming','Wyoming')
        )
class NameSearch(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    state = models.CharField(max_length=20, choices=STATES, default='green')

    def __str__(self):
        return f'search{self.first}'