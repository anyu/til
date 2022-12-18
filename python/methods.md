# Methods

Always use `self` for the first argument to instance methods.
Always use `cls` for the first argument to class methods.

Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called. Since the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self . However, class methods can still modify class state that applies across all instances of the class.
