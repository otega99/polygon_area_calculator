class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height

  def set_width(self,width):
    self.width=width

  def set_height(self,height):
    self.height=height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return (2*self.width+2*self.height)

  def get_diagonal(self):
    return ((self.width ** 2 +self.height **2)**.5)

  def get_picture(self):
    if self.width>50:
      return "Too big for picture."
    else:
      str1=""
      for i in range(0,self.height):
        str1+="{}\n".format("*"*self.width)
      return str1

  def get_amount_inside(self,rectangle):
    return self.get_area()//rectangle.get_area()

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)

class Square(Rectangle):
  def __init__(self,length):
    self.width=length
    self.height=length

  def set_side(self,new_length):
    self.width=new_length
    self.height=new_length

  def set_width(self,new_length):
    self.width=new_length
    self.height=new_length

  def set_height(self,new_length):
    self.width=new_length
    self.height=new_length

  def __str__(self):
    return "Square(side={})".format(self.width)