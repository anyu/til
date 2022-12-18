# Test Doubles (umbrella term)

Super useful article: https://8thlight.com/blog/uncle-bob/2014/05/14/TheLittleMocker.html

- Fakes
  - actually has business logic (rarely used, but term often used loosely in place of other doubles)
  - most different from the others
- Mocks
  - like counterfeiter (kind of like a stub+spies)
  - like a stub that spies
  - spies on the behavior of the module being tested. And the mock knows what behavior to expect.

- Spies
  - spies on the caller (checks that a function was called, with X args, etc)
  - differentiation between mocks: after a program has run (mocks - as a program IS running)
- Stubs
  - returns specific result / hardcode output you want (a function that returns true/false, or some object you want)

- Dummy
  - doesn’t do anything (a function that returns nil)
  - doesn’t care if never called

Stubs and spies most often used


