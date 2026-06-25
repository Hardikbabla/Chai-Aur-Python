import arrow

brewing_time = arrow.utcnow()
print(brewing_time)
rome_time = brewing_time.to("Europe/Rome")
print(rome_time)


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
my_point = Point(10, 20)

print(f"X coordinate: {my_point.x}")
print(f"Y coordinate: {my_point.y}")
