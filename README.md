# Data Processing and Storage Assignment

## Description
This project implements a simple in-memory database in Python that supports transactions. The database allows for operations such as beginning a transaction, updating and retrieving values, and committing or rolling back changes.

- **Comprehensive Testing**: Each test within the `main()` function is carefully described with a short sentence explaining its purpose. This includes attempts to perform operations like updating or retrieving values both within and outside of transactions, and more.
- **Visibility of Operations**: Throughout the execution of these tests, I output the current state of the main database after each test to show the effect of each operation. This transparency is to help you understand how each test influences the database state and so that you can be aware of the state of the main database at all times throughout my entire code. 
- **Interactive Output**: For each action, whether starting a transaction, updating a key, committing, or rolling back, there are print statements that clearly show what function is being executed. This real-time feedback makes it easier to trace the flow of data and operations.
- **Verification and Comparison**: I encourage you, the grader, to copy the entire class along with its functions to test against your own code if you have any doubts or just want to see for yourself.

## How to Run the Code

### Prerequisites
- Python 3.x installed on your machine.

### Running the Program
1. Clone my repository to your local machine
2. Navigate to the directory where you have my code
3. Run my program with Python (python main.py) or (py main.py)

## Future Modifications for Assignment
To take this assignment to the next level and have it as an official assignment in the future, I recommend starting by making the instructions more clear. I was confused the entire time about whether we only needed to write the functions themselves, or also include a main function so that the code just outputs the results for each test I create. I also think it would help if specific test cases are included so that the student can easily just test their code using those test cases. I wasn't sure if we had to create our own tests or not, but I ended up hardcoding a bunch of tests, which forced me to spend more time on the assignment even though I was already done with the actual code's functionality a while ago. Furthermore, since the grader will just be seeing the tests that I created, the grading process isn't as optimized as it could potentially be in the near future. Developing some kind of grading script to automatically run and validate predefined test cases (that the professor should include) would streamline the grading process and guarantee consistency.

