# Predict.
A University requires a program to predict progression outcomes at the end of each academic year.

The program should allow students to predict their progression outcome at the end of each academic year. The
program should prompt for the number of credits at pass, defer and fail and then display the appropriate
progression outcome for an individual student (i.e., progress, trailing, module retriever or exclude).

The program should display ‘Integer required’ if a credit input is the wrong data type.
The program should display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80,
100 and 120.
The program should display ‘Total incorrect’ if the total of the pass, defer and fail credits is not 120.
A few marks will be allocated for the efficient use of condi􀆟onal statements. For example, the
program does not need 28 condi􀆟onal statements for 28 outcomes.

The program loops to allow a staff member to predict progression outcomes for mul􀆟ple students.
The program should prompt for credits at pass, defer and fail and display the appropriate progression
for each individual student un􀆟l the staff member enters ‘q’ to quit. Op􀆟onally you can use an input of
‘y’ to con􀆟nue.

When ‘q’ is entered, the program should use the “graphics.py” module to produce a ‘histogram’
represen􀆟ng the number of students who achieved a progress outcome in each category range:
progress, trailing, module retriever and exclude. The histogram should relate to the data input entered
during the program run and work for any number of outcomes, it must use the graphics.py module.
Display the number of students for each progression category and the total number of students.
Example of a program run and input (in bold). Note: program should exit on ‘q’ to quit and produce the
histogram. ‘y’ to con􀆟nue shown in the example is op􀆟onal and depends on your program structure.

For this part you could create an addi􀆟onal Part 3 program or extending your original version. Use
python to save any inpu􀆩ed progression data to a text file. Later in the program, access the stored
data and print out as shown below. Test plan not required. Example output (with data from text file):

