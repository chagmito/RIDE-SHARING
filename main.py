from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Rider, Driver
from vehicle import Car, Bike

niye_jaou = RideSharing('Niye Jaou')
rahim = Rider('Rahim Uddin', 'rahim@gamil.com', 1234, 'mohakhali', 1200)
niye_jaou.add_rider(rahim)
karim = Driver('Karim uddin', 'karim@gami.com', 1256, 'gulshan')
niye_jaou.add_driver(karim)
rahim.request_ride(niye_jaou, 'uttara', 'car')
karim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
