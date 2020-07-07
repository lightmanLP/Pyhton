class Foo:
  """Класс для проверки лайфхака)"""
  a: dict = {}
  b: list = []

  def get_data(self):
    return self.a, self.b

  def add_data(self):
    self.a.update({'foo': 'bar'})
    self.b.append('foo')


# создаем 2 пустых объекта одного класса
foo1 = Foo()
foo2 = Foo()

# добавляем данные одному из них
foo1.add_data()


# выводим данные из объектов
for i in foo1, foo2:
  print(*i.get_data())

# и из класса
print(Foo.a, Foo.b)

# >>> {'foo': 'bar'} ['foo']
# >>> {'foo': 'bar'} ['foo']
# >>> {'foo': 'bar'} ['foo']