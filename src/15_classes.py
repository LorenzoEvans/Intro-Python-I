# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
 def __init__(self, lat, lon):
  self.lat = lat
  self.lon = lon

exp_latlon = LatLon(88, 90)

print(exp_latlon.lat)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
 def __init__(self, lat, lon, name):
  super().__init__(name, lon)
  self.lat = lat
  self.lon = lon
  self.name = name
 def __repr__(self):
  return "Waypoint: lat: %s lon: %s name: %s" % (self.lat, self.lon, self.name)

exp_waypoint = Waypoint(82, 90, 'place')
print('name:', exp_waypoint.lat)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
 def __init__(self, lat, lon, difficulty, size, name):
  super().__init__(difficulty, size, name)
  self.difficulty = difficulty
  self.size = size

exp_geocache = Geocache(12, 34, 'hard', 900, 'terrain')
print(exp_geocache.size)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(41.70505, -121.51521, 'Catacombs')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
