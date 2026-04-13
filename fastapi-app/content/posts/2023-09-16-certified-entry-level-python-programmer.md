---
layout: post
title: How I Became a Certified Python Programmer
description: Python Certified Entry-Level Programmer (PCEP)
tags: python 
categories: self-taught-programmer
---

My summer hard-studying efforts finally paid off with the Python Certified Entry-Level Programmer (PCEP) certification. Here's a sneak peek of how things went!

I've kept myself busy during these past few months with studying hard to get my PCEP certification from the Python Institute. They offer the learning resources for free under the ["Python Essentials 1 Aligned with PCEP-30-02"](https://pythoninstitute.org/python-essentials-1) collection, PCEP-30-02 being the latest revision of the PCEP exam. Their materials are decent and make for a useful recap for someone like me who already has some experience under the belt. They are exclusively text-based, but they come along with a decent IDE and Sandbox environment for practicing. I managed to learn a thing or two on top of the recap. All in all, I'm happy with the overall platform experience. 

**And yes! I passed the exam with a 96% score!** You can check my PCEP certificate [here](https://verify.openedg.org/?id=ECr2.VJbN.6JfQ). 

Next milestone on my list is the Certified Associate in Python Programming (PCAP) certification. The workflow is similar, but the topics are a tad more advanced, with a lot of focus on Object Oriented Programming (OOP), managing exceptions and constructing more advanced and useful programs. For example, just now I've completed the latest lab from the ["Python Essentials 2 Aligned with PCAP-31-03"](https://pythoninstitute.org/python-essentials-2) learning resources. This lab is using class composition, private instance properties and dunder methods such as the _constructor_ and _str_ that are used for instantianting new objects, respectively for custom string formatting. I completed the lab's expectations and then some. At this level math skills are becoming necessary and they can be quite challenging at times, but it's the same as with everything else: *where there's a will, there's a way!* I'm also targeting my math and logical skills using the [Brilliant](https://brilliant.org/) app. You should really give it a try as it presents a gamified and highly interactive approach that makes learning the most difficult Science Technology Engineering and Math (STEM) concepts a breeze.

I leave you with my solution code for the latest lab `3.4.1.15 Triangle` I was just telling you about:

```python
'''
This program can calculate the side lengths, perimeter and the area of a triangle
based on an input that defines the Triangle's 3 vertices in the Cartesian
space:
* each point/vertice has its own (x, y) coordinates such as: Point(3, 2)
* each triangle is composed of 3 points/vertices such as: Triangle(Point(0, 0),
Point(1, 0), Point(0, 1))

The area is calculated using Heron's formula:
* calculate the triangle's 3 sides: a, b, c; use Point.distance_from_point()
* calculate the semiperimeter: s = (a + b + c) / 2; use Triangle.perimeter() / 2
* calculate the area: math.sqrt(s * (s - a) * (s - b) * (s - c))
'''
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_point(self):
      return (self.__x, self.__y)

    def getx(self):
      return self.__x

    def gety(self):
      return self.__y

    def distance_from_xy(self, x, y):
      return math.sqrt((x - self.__x)**2 + (y - self.__y)**2)

    def distance_from_point(self, point):
      return math.sqrt((point.__x - self.__x)**2 + (point.__y - self.__y)**2)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
      # define the vertices using Cartesian coordinates (x, y)
      self.__vertice1 = vertice1
      self.__vertice2 = vertice2
      self.__vertice3 = vertice3

      # get the length of the triangle's 3 sides
      v1, v2, v3 = self.__vertice1, self.__vertice2, self.__vertice3
      self.__side1 = v1.distance_from_point(v2)
      self.__side2 = v2.distance_from_point(v3)
      self.__side3 = v3.distance_from_point(v1)

    def __str__(self):
      return f"""This triangle is defined by:
  * 3 sides measuring: {self.__side1:.2f}, {self.__side2:.2f}, {self.__side3:.2f};
  * a perimeter of: {self.perimeter():.2f};
  * an area of: {self.area():.2f}.\n"""

    def perimeter(self):
      return self.__side1 + self.__side2 + self.__side3

    def area(self):
      # 1. calculate the semiperimeter
      s = self.perimeter() / 2
      # 2. calculate the area using Heron's formula
      area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
      return area


# Use composition to create 1 Triangle instance based on 3 Point instances (x, y)
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle)
print(f"The triangle's perimeter is: {triangle.perimeter()}.")
print(f"The triangle's area is: {triangle.area()}.")

```

... and a sample output:

```
This triangle is defined by: 
* 3 sides measuring: 1.00, 1.41, 1.00; 
* a perimeter of: 3.41; 
* an area of: 0.50. 

The triangle's perimeter is: 3.414213562373095. 
The triangle's area is: 0.49999999999999983.
```
