class Sphere(object):
	p=3.14
	def __init__(self, radius=1, x=0, y=0, z=0):
		self.radius=radius; self.x=x; self.y=y; self.z=z
	def get_radius(self):
		return self.radius
	def get_volume(self):
		return(4.0/3.0*(self.p*(self.radius**3)))
	def get_square(self):
		return(4*(self.p*(self.radius**2)))
	def get_center(self):
		return(self.x, self.y, self.z)
	def set_radius(self, r):
		self.radius=r
	def set_center(self,x1,y1,z1):
		self.x=x1; self.y=y1; self.z=z1
	def is_point_inside(self,x,y,z):
		if ((self.x-x)**2+(self.y-y)**2+(self.z-z)**2)<=self.radius**2:
			return True
		else:
			return False


a=Sphere(5)
print ('Метод get_radius = ',a.get_radius())
print ('Метод get_volume = ',a.get_volume())
print ('Метод get_square = ',a.get_square())
print ('Метод get_center = ',a.get_center())
print ('Метод is_point_inside = ',a.is_point_inside(0,0,6))
a.set_radius(6)
print ('Метод get_radius = ',a.get_radius())
print ('Метод is_point_inside = ',a.is_point_inside(0,0,6))

