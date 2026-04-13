---
layout: post
title: Becoming a Certified Professional in Python Programming
description: Certified Professional in Python Programming (PCPP)
tags: python 
categories: self-taught-programmer
---

It's been a while since I last posted on my blog, but that doesn't mean I've been idle—not in the slightest! Yesterday, I completed the last of the five courses from the Python Institute's Certified Professional in Python Programming (PCPP) curriculum.

Here are the courses I've covered from the Python Institute:
* [Python Essentials 1](https://pythoninstitute.org/python-essentials-1) - 42 hours
* [Python Essentials 2](https://pythoninstitute.org/python-essentials-2) - 58 hours
* [Python Professional 1](https://pythoninstitute.org/python-professional-1) - 119 hours split into 5 modules:
    * Advanced Classes and Object-Oriented Programming in Python
    * Best Practices and Standardization
    * Introduction to GUI Programming in Python (TkInter)
    * Working with RESTful APIs
    * Processing different kinds of text files

I haven't yet taken the certification exam for PCPP. I haven't decided if it's worth the cost and hassle. I tend to think there are more important priorities now, such as:
* Applying my acquired knowledge at work (e.g., small scripts, automation)
* Tackling Leetcode problems for that all-important glory and hubris
* Finding a personal project that excites me or contributing to an open-source project

The important part is to keep at it, be consistent, and treat programming as an enjoyable hobby. The rest will follow, won't it? Cheers!

PS: Here is some of that hubris manifesting itself. I did not only solve the [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/description/) problem on my own (no ChatGPT, no StackOverflow, not even the official Python documentation), but according to Leetcode my solution beat 86% of the other submissions on runtime speed. Yes, the problem is not that difficult, but it would've been impossible for me to tackle without assistance just a year ago. Here follows my solution:

```python

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Flip the image horizontally
        flipped_image = list()
        for row in image:
            flipped_image.append(row[::-1])

        # Invert the image (0 becomes 1, 1 becomes 0)
        inverted_flipped_image = list()
        for row in flipped_image:
            inverted_row = list()
            for pixel in row:
                if pixel == 1:
                    inverted_pixel = 0
                else:
                    inverted_pixel = 1
                inverted_row.append(inverted_pixel)
            inverted_flipped_image.append(inverted_row)

        # Return the flipped and inverted image
        return inverted_flipped_image
```
