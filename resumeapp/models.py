from django.db import models

# Create your models here.


class Resume(models.Model):

    STATE_CHOICE = (
      
('Andhra Pradesh',	'Amaravati	'),
('Arunachal Pradesh'	,'Itanagar'),
('Assam',	'Dispur'),
('Bihar'	,'Patna'),
('Chhattisgarh',	'Raipur'),	
('Goa'	,'Panaji'),	
('Gujarat'	,'Gandhinagar'),	

    )
    name = models.CharField(max_length=120)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    pincode = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=120)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_location = models.CharField(max_length=120)
    profile_image = models.ImageField(upload_to = 'images',blank=True,null=True)
    job_state = models.CharField(max_length=20)
    my_file = models.FileField(upload_to='doc',blank=True)
