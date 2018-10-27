1.	List your name and email address.

NAME: HaYoung Kyung
EMAIL: hkyung@hsph.harvard.edu
GITHUB REPOSITORY URL: 
I emailed Eric about the issue I’m having with creating a private repository on Github. In order to make my Github account into a student developer account, I had to send in documents to verify my student status. This apparently takes up to 5 days for approval. I have set my repository to public for now, and will set it to private as soon as possible.

2.	Summarize your experience working on the final project. For example, you might approximate how many hours you spent on it and how those hours were distributed. If you found some aspects considerably harder than others, list those here. If there are known problems with your final project script, list those here.

ANSWER: The final project taught me useful skills that I can apply in my academic and research career. I am now able to take data sets and create nice visual representations. I worked on this project for 3 days, about 3-4 hours each day. I spent about 1 hour trying to understand matplotlib, 5 hours writing the script, and 3 hours fixing errors in my script. It would be nice to have had an in class tutorial on matplotlib. I struggled learning this on my own (finding the most useful tutorial).

3.	In a few sentences, describe what your final project script does.

ANSWER: scatter.py takes in a path to the input file, an int value indicating the column for the x values, an int value indicating the column for the y values, an optional int value indicating the column for categorical (stratified) values, and an optional path to the output file. If the column to stratify is not provided by the user, then we plot the columns of x and y values as one series. If the column to stratify is provided by the user, then we plot the columns of x and y values for each categorical value in the stratify column. A legend is provided to provide the relationship between the colors and the categorical values.

4.	List any modules (outside of the Python standard library) that are required to execute your final project script. You may answer “N/A” if no such modules are required.

ANSWER: N/A

5.	Describe your sample INPUT FILE(S). If you are completing a custom final project that does not require an input file, explain that clearly here.

ANSWER: I used diamonds_reduced.tsv as my sample input file. This sample input file has 10 columns for variables carat, cut, color, clarity, depth, table, price, x, y, and z. The columns we can stratify are the categorical columns: cut, color, and clarity. The x values can be selected from all other columns (carat, depth, table, price, x, y, and z). The y values can also be selected from all other columns that are neither the stratify columns nor the x value column. 

6.	Provide the command used to produce your sample OUTPUT FILE with flags and arguments specified (e.g. “$ python script_name.py arguments”).

ANSWER: $ python ./scatter.py diamonds_reduced.tsv --x_value 1 --y_value 7 --strat 2 --output 172.png

7.	Describe your sample OUTPUT FILE(S). If you are completing a custom final project that does not produce an output file, capture the STDOUT of the command specified above and include it here (e.g. “$ command > sample_stdout.txt”).

ANSWER: I chose the carat column to be my x values and price column to be my y values. The cut column was selected for my stratified mode. This generated an output file (172.png) that displays a scatter plot of price over carat, stratified by diamond cut. 

8.	What was your favorite part of learning to program in BST 273 (i.e. something we should definitely NOT change in future incarnations of the course)?

ANSWER: My favorite part was completing homework assignments. They were challenging but I learned a lot!

9.	What was your LEAST favorite part of learning to program in BST 273 (i.e. something we should look into changing for future incarnations of the course)?

ANSWER: I think it would be more helpful to have a more substantial “lab” section in class, much like the live coding sessions we had for some lectures.