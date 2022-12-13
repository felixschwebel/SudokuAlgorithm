# SudokuAlgorithm
An algorithm for solving Sudokus which uses the Tkinter module to create a graphical user interface. The idea for this project came in an Information-Management-lecture where we solved Sudokus by hand in preparation for the lecture on sorting algorithms. 

**It just works for easy and medium Sudokus when only one step involes guessing.** 

For the user inputs, I used the Canvas object from the Tkinter module. It displays an empty Sudoku grid and generates 81 input fields with 2 for-loops. 

<img width="698" alt="Screenshot 2022-12-13 at 17 52 31" src="https://user-images.githubusercontent.com/111788725/207394860-9047c4f9-1d74-4e7a-bb8b-c4d42803b6ca.png">

When the solve button is pressed all the data is fetched and added to a list of dictionaries. These **dictionaries contain the index, the value, the quadrant, the row, the column, and a list of possible values**. If a field has a value, the possible value list will be empty.

The solve-function starts by checking the quadrant, rows, and columns for each field. All the found values in the same quarter, row or column are then removed from the possible-values list.

<img width="694" alt="Screenshot 2022-12-13 at 17 53 27" src="https://user-images.githubusercontent.com/111788725/207395077-de794027-ccb6-4389-97f8-724d3f103c9d.png">

If a field has just one possible value this value will be assigned to the field. Unfortunately, that only works for Sudokus if there is no guessing involved. 

<img width="432" alt="Screenshot 2022-12-13 at 17 54 22" src="https://user-images.githubusercontent.com/111788725/207395241-5fc7372a-908e-4227-9b96-5fa9ad933bb9.png">

If there were no values assigned to any field and the game is not over, all the data will be backed up before guessing. Then all the fields with 2 possible values are checked. 


<img width="691" alt="Screenshot 2022-12-13 at 17 55 57" src="https://user-images.githubusercontent.com/111788725/207395561-2240350e-0770-4cd1-9681-992afc489906.png">
<img width="480" alt="Screenshot 2022-12-13 at 17 58 54" src="https://user-images.githubusercontent.com/111788725/207396288-5a6b41a4-d010-4d00-8744-03eb3473fe8c.png">

This only works for easy and medium difficult Sudokus and very rarely for hard ones, because after the first guess all other steps must be assigned directly otherwise the program will revert to the backed-up data and try again. The checked values that didn’t lead to a result are saved in a list as well. 

In the future, I want to implement the saving of multiple versions so that the guessing can be repeated. For harder Sudokus, it also maybe required to guess for fields which have more than 2 possible values. 
