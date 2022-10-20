

class Spring:
	def __init__(self, spring_name: str, load_level: int, longitude: float, latitude: float):
		self._spring_name = spring_name
		self._load_level = load_level
		self._longitude = longitude
		self._latitude = latitude
		
	def get_spring_name(self):
		return self._spring_name

	def set_spring_name(self, new_spring_name):
		self._spring_name = new_spring_name

	def get_load_level(self):
		return self._load_level

	def set_load_level(self, new_load_level):
		self._load_level = new_load_level

	def get_longitude(self):
		return self._longitude

	def set_longitude(self, new_longitude):
		self._longitude = new_longitude

	def get_latitude(self):
		return self._latitude

	def set_latitude(self, new_latitude):
		self._latitude = new_latitude
