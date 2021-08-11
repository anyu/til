# Java Interfaces

## Functional interfaces

- An interface that contains only 1 abstract method
- (Java 8+) Can use lambda exprssions to represent an instance of a functional interface
  ```java
  class Test
  {
    public static void main(String args[]) {
      new Thread(()-> {
        System.out.println("New thread created");
      }).start();
    }
  }
  ```
