#ifndef MYMATH_H_
#define MYMATH_H_

class MyMath {
public:
  // Inline functions for basic operations
  inline static double add(double a, double b) {
    return a + b;
  }
  inline static double subtract(double a, double b) {
    return a - b;
  }
  inline static double multiply(double a, double b) {
    return a * b;
  }
  inline static double divide(double a, double b) {
    return a / b;
  }

  // Non-inline function for a more complex operation
  double calculateAreaOfCircle(double radius) {
    return PI * radius * radius;
  }

private:
  static constexpr double PI = 3.14159265358979323846;
};


#endif // MYMATH_H_
