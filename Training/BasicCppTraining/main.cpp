#include <iostream> //Imports cout
#include <sstream>
#include <string>
#include "Person.h"

void compareAnswers(const std::string myAnswer, const std::string correctAnswer)
{
    if (myAnswer.compare(correctAnswer) != 0)
    {
        std::cout << "Incorrect." << std::endl
                  << "Expected: " << correctAnswer << std::endl
                  << "You got: " << myAnswer << std::endl;
    }
    else
    {
        std::cout << "Correct." << std::endl;
    }
}
// Swaps a & b.
void mySwap(int& a, int& b)
{
}
// Increment the int that x is pointing to by one.
void myIncrement(int* x)
{
}

// Uncomment this when person.cpp has been created.
/* void personFunctions()
{
    Person Bill;
    Bill.setName("Bill");
    Bill.setAge(18);
    Bill.printInfo();
    Person Bob("Bob", 30);
    Bob.printInfo();
    Person* Joe = new Person("Joe", 15);
    Joe->printInfo();
    Person* personArray[] = {&Bill, &Bob, Joe};
    std::stringstream myCombinedAgeAnswer;
    myCombinedAgeAnswer << "The combined age of Bill, Bob, and Joe is: " << Person::combinedAge(personArray, sizeof(personArray) / sizeof(Person*));
    const std::string correctCombinedAgeAnswer = "The combined age of Bill, Bob, and Joe is: 63";
    std::cout << "Checking Person::combinedAge:" << std::endl
              << myCombinedAgeAnswer.str() << std::endl;
    compareAnswers(myCombinedAgeAnswer.str(), correctCombinedAgeAnswer);
    Person::birthday(Bill);
    std::stringstream myBirthdayAnswer;
    myBirthdayAnswer << "It was Bill's Birthday, he is now " << Bill.getAge();
    const std::string correctBirthdayAnswer = "It was Bill's Birthday, he is now 19";
    std::cout << "Checking Person::Birthday:" << std::endl
              << myBirthdayAnswer.str() << std::endl;
    compareAnswers(myBirthdayAnswer.str(), correctBirthdayAnswer);
    delete Joe;
}*/

int main()
{
    int a = 5;
    int b = 6;
    std::stringstream swapIncrementAnswer;
    std::cout << "Checking Swap and Increment: " << std::endl;
    swapIncrementAnswer << "a is " << a << ", b is " << b;
    std::cout << swapIncrementAnswer.str() << std::endl;
    const std::string correctSwapIncrementAnswer = "a is 7, b is 5";
    compareAnswers(swapIncrementAnswer.str(), correctSwapIncrementAnswer);
// Pass a & b into mySwap
// Pass in a to myIncrement
    //personFunctions(); // Uncomment this once you have completed the definitions of the Person class.
    return 0;
}
