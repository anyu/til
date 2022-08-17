# Python Underscore Syntax

| Example     | Description |
| ----------- | ----------- |
| `_foo`      | single **leading** underscore                           |
| `foo_`      | single **trailing** underscore                          |
| `_`         | single underscore                                       |
| `__foo__`   | double **leaading**, double **trailing** underscores    |
| `__foo`     | double **leading** underscores                          |


## `_foo`:  Single leading underscore

- for internal objects
- a syntax hint that's not enforced by the interpreter, so technically still accessible externally.
  - EXCEPT by default, a variable with a single leading underscore won't be available in the namespace for wildcard imports.
    ```py
    from module import *

    _private_variable # will get error that _private_variable isn't defined
    ```
  - But it **can** be accesssed if you import the module and call the variable directly
    ```py
    import module

    module._private_var
    ```

## `foo_`: Single trailing underscore

- to use a var name that's a reserved Python keyword

## `_`: Single underscore

- to define temporary or unused variables
  ```py
  for _ in range(10):
      do_work()
  ```
- to visually separate numeric literals
  ```py
  1_000_000_000
  ```

## `__foo__`: Double leading and trailing underscores

- aka. double underscore methods, dunder methods
- reserved methods with special behavior that you can overwrite:
  - `__init__`: class constructor
  - `__call__`: make object callable
  - `__str__`: define what's printed when `print` calls the object

## `__foo`: Double leading underscores

- used for **name mangling**, where the interpreter changes the name to avoid collisions in subclasses
  ```py
  class Car:
    def __init__(self):
        self.color = "red"
        self._speed = 70
        self.__brand = "bmw"

  car = Car()
  ```

  ```py
  >>> print(dir(car))

  [...'_Car__brand', '_speed', 'color'...]
  ```

  The interpreter does this to avoid `__brand` being overridden by subclasses:

  ```py
  class ExtendedCar(Car):
      def __init__(self):
          super(ExtendedCar, self).__init__()
          self.color = "green"
          self._speed = 80
          self.__brand = "audi"

  extended_car = ExtendedCar()
  ```

  ```py
  >>> print(dir(extended_car))

  ['_Car__brand', '_ExtendedCar__brand', ... '_speed', 'color']
  ```

  ```py
  >>> extended_car._Car__brand
  'bmw'

  >>> extended_car._ExtendedCar__brand
  'audi'
  ```
