from sample import parent
class child(parent):
    def display(self):
      a = self.add(4,5)
      b = self.mul(2,50)
      c = self.div(25,5)
      d = self.sub(14,7)
      print(a)
      print(b)
      print(c)
      print(d)

x = child()
x.display()