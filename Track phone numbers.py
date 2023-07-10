import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


code="+91 ##########"

country_name=phonenumbers.parse(code,"CH")
print(geocoder.description_for_number(country_name,"en"))

service_num=phonenumbers.parse(code,"RO")
print(geocoder.description_for_number(service_num,"en"))


time_zone=phonenumbers.parse(code,"GB")
print(timezone.time_zones_for_number(time_zone))





