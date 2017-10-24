#pragma once

#include <string>

class Person
{
public:
    Person();
    ~Person();
    Person(const std::string& name, int age);

    // setters and getters
    int getAge() const;
    const std::string& getName() const;
    void setName(const std::string& newName);
    void setAge(int newAge);

    // Print out the name and age of the person.
    void printInfo() const;
    // Print the combined age of everyone pointed to by personArray
    static int combinedAge(Person** personArray, int size);
    // Increases the Person's Age by 1.
    static void birthday(Person& x);

private:
    std::string name_;
    int* age_; // age_ should be a dynamically allocated.

};


