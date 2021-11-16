from django.db import models

# Create your models here.
class School(models.Model):
    code = models.IntegerField(default=1000000) # 7 digit integer
    html = models.TextField()

    def __str__(self) -> str:
        resp = f'{self.code}'
        if self.html == 'no data':
            resp += '(empty)'
        return resp

class CeleryTasks(models.Model):
    started = models.DateTimeField()
    finished = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    def __str__(self) -> str:
        end = self.finished.strftime('%Y-%m-%d %H:%M:%S%z') if self.finished else ''
        return f'{self.name} {self.started:%Y-%m-%d %H:%M:%S%z} to {end}'


# class Address(models.Model):	
# 	state = models.CharField(max_length=60)
# 	district = models.CharField(max_length=60)
# 	block = models.CharField(max_length=60)
# 	cluster = models.CharField(max_length=60)
# 	village = models.CharField(max_length=60)
# 	pincode = models.CharField(max_length=6) # six digit pincode
	

class School2(models.Model):
	"""
	school_category: {
		'10-Secondary with Higher Secondary': 2717,
		'11-Higher Secondary only/Jr. College': 10,
		'1-Primary': 68182,
		'2-Primary with Upper Primary': 25853,
		'3-Pr. with Up.Pr. Sec. and H.Sec.': 2062,
		'4-Upper Primary only': 15863,
		'5-Up. Pr. Secondary and Higher Sec': 3857,
		'6-Pr. Up Pr. and Secondary Only': 3927,
		'7-Upper Pr. and Secondary': 2048,
		'8-Secondary Only': 2192
	}
	school_type: {'1-Boys': 598, '2-Girls': 1987, 
		'3-Co-educational': 124126}
	

	{'101-Other Central Govt. Schools': 2, '17-KGBV': 295, '1-Department of Education': 24019, '1-Dept. Of education': 54438, 
		'2-Tribal Welfare Department': 225, '3-Local Body': 52, '4-Government Aided': 30, '4-Govt. aided': 3120, 
		'5-Private Unaided (Recognized)': 5697, '5-Pvt. Unaided (Recognized)': 32164, '6-Other Govt. Managed schools': 6, 
		'8-Unrecognized': 39, '90-Social Welfare Dept.': 27, '91-Ministry of Labour': 2, '92-Central School': 45, '92-Kendriya Vidyalaya': 39, 
		'93-Jawahar Navodaya Vidhyalaya': 42, '93-Jawahar Navodaya Vidyalaya': 19, '97-Madarsa recognized (by Wakf board/Madarsa Board)': 68, 
		'97-Madarsa Recognized (by Wakf board/Madarsa Board)': 5387, '98-Madarsa unrecognized': 5, '98-Madarsa Unrecognized': 990}
	state_management

	{'101-Other Central Govt Managed Schools': 2, '1-Department of Education': 78752, '2-Tribal Welfare Department': 225, '3-Local body': 52, 
		'4-Government Aided': 3150, '5-Private Unaided (Recognized)': 37861, '6-Other Govt. Managed Schools': 6, '8-Unrecognized': 39, 
		'90-Social welfare Department': 27, '91-Ministry of Labor': 2, '92-Kendriya Vidyalaya': 84, '93-Jawahar Navodaya Vidyalaya': 61, 
		'97-Madarsa recognized (by Wakf board/Madarsa Board)': 5455, '98-Madarsa unrecognized': 995}
	national_management

	{'': 26687, '1-Yes': 20989, '2-No': 79035}
	pre_primary

	{'10-School running in other Department Building': 161, '1-Private': 41820, '2-Rented': 7494, '3-Government': 73799, 
		'4-Government school in a rent free building': 2863, '5-No Building': 356, '7-Building Under Construction': 218}
	building_status

	{'1-Pucca': 74648, '2-Pucca but broken': 8648, '3-Barbed wire fencing': 1451, '4-Hedges': 696, '5-No boundary walls': 35335, 
		'6-Others': 1019, '7-Partial': 3625, '8-Under Construction': 1289}
	boundary_wall

	{'Yes': 126711}
	drinking_water_availability

	{'Yes': 126711}
	hand_wash_facility

	{'1-Yes': 67160, '2-No': 59551}
	library

	{'1-Yes': 22771, '2-No': 103940}
	reading_corner

	{'1-Yes': 56159, '2-No': 70552}
	book_bank

	{'1-Yes': 15332, '2-No': 111379}
	internet

	{'1-Yes': 4025, '2-No': 122686}
	dth

	"""
	code = models.IntegerField(default=1000000) # 7 digit integer
	school_name = models.CharField(max_length=200)
	udise_code = models.CharField(max_length=11) # 11 digit integer may starts with 0
	
	# address
	state = models.CharField(max_length=60)
	district = models.CharField(max_length=60)
	block = models.CharField(max_length=60)
	cluster = models.CharField(max_length=60)
	village = models.CharField(max_length=60)
	pincode = models.CharField(max_length=6) # six digit pincode
	
	school_category = models.CharField(max_length=60)
	school_type = models.CharField(max_length=60)
	class_from = models.SmallIntegerField()
	class_to = models.SmallIntegerField()
	state_management = models.CharField(max_length=200) #5-Private Unaided (Recognized)
	national_management = models.CharField(max_length=200)
	status = models.CharField(max_length=60)
	location = models.CharField(max_length=60)
	aff_board_sec = models.CharField(max_length=60)
	aff_board_hsec = models.CharField(max_length=60)
	year_of_establishment = models.SmallIntegerField()
	pre_primary = models.CharField(max_length=10)
	building_status = models.CharField(max_length=60)
	boundary_wall = models.CharField(max_length=60)
	no_of_boys_toilets = models.SmallIntegerField()
	no_of_girls_toilets = models.SmallIntegerField()
	no_of_cwsn_toilets = models.SmallIntegerField()

	# need to remove these two fields since all values are yes
	drinking_water_availability = models.BooleanField(default=True) # yes no
	hand_wash_facility = models.BooleanField(default=True) #yes

	functional_generator = models.SmallIntegerField()
	library = models.BooleanField(default=True)
	reading_corner = models.BooleanField(default=True)
	book_bank = models.BooleanField(default=True)
	functional_laptop = models.SmallIntegerField()
	functional_desktop = models.SmallIntegerField()
	functional_tablet = models.SmallIntegerField()
	functional_scanner = models.SmallIntegerField()
	functional_printer = models.SmallIntegerField()
	functional_led = models.SmallIntegerField()
	functional_digiboard = models.SmallIntegerField()
	internet = models.BooleanField(default=True)
	dth = models.BooleanField(default=True)
	functional_web_cam = models.SmallIntegerField()
	class_rooms = models.SmallIntegerField()
	other_rooms = models.SmallIntegerField()
	enrolment_of_the_students = models.CharField(max_length=60)
	total_teachers = models.SmallIntegerField()
