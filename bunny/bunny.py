'''
-Problem-
Input: An N x M matrix of a garden. Each cell contains an integer representing the number of carrots in that part of the garden.

Output: The number of carrots Bunny eats before falling asleep.

Conditions: Bunny starts in the center of the garden. 
1. If there are more than one center cell, Bunny starts in the cell with the largest number of carrots. 
2. There will never be a tie for the highest number of carrots in a center cell. 
3. Bunny eats all of the carrots in his cell, then looks left, right, up, and down for more carrots. 
4. Bunny always moves to the adjacent cell with the highest carrot count. 
5. If there are no adjacent cells with carrots, Bunny falls asleep.

-Assumptions for this problem-
1. Number of carrots in cells are positive integers
2. All input fields are on-empty arrays
3. Run Python 3.6.1 environment

Run command:
python bunny.py
'''

import numpy as np
from test_bunny import *

'''
find_start
<-Takes in N x M field array
->Return Bunny's starting position depending
  on the 4 types of N x M input
'''
def find_start(field):
  # Type array to an np array so I can use its functions
  field = np.array(field)

  # Number of rows and columns in the given array
  num_rows = field.shape[0]
  num_cols = field.shape[1]

  # Case: Odd Rows x Odd Columns -> [x]
  if num_rows % 2 != 0 and num_cols % 2 != 0:
    # Get center indices
    start_row = int((num_rows - 1) / 2)
    start_col = int((num_cols - 1) / 2)

  # Case: Even Rows x Odd Columns -> [x x]
  elif num_rows % 2 == 0 and num_cols % 2 != 0:
    # Set index of starting column
    start_col = int((num_cols - 1) / 2)

    # Set center row's upper and lower bounds for temp array
    row_lower = int((num_rows/2) - 1)
    row_upper = int(num_rows/2) + 1
    # temp array contains only the center values
    temp = field[row_lower:row_upper, start_col]
    # Get max center value's index from the temp array
    idx = np.unravel_index(temp.argmax(), temp.shape)
    # Set index of starting row
    start_row = idx[0] + row_lower
  
  # Case: Odd Rows x Even Columns -> [x],[x]
  elif num_rows % 2 != 0 and num_cols % 2 == 0:
    # Set index of starting row
    start_row = int((num_rows - 1) / 2)
    # Set center column's upper and lower bounds for temp array
    col_lower = int((num_cols/2) - 1)
    col_upper = int(num_cols/2) + 1
    # temp array contains only the center values
    temp = field[start_row, col_lower:col_upper]
    # Get max value's index from the temp array
    idx = np.unravel_index(temp.argmax(), temp.shape)
    # Set index of starting column
    start_col = idx[0] + col_lower

  # Case: Even Rows x Even Columns -> [x x], [x x]
  else:
    # Need to get max value from a 2x2 center
    col_lower = int((num_cols/2) - 1)
    col_upper = int(num_cols/2) + 1
    row_lower = int((num_rows/2) - 1)
    row_upper = int(num_rows/2) + 1
    # Get max value's index from the temp array
    temp = field[row_lower:row_upper, col_lower:col_upper]
    idx = np.unravel_index(temp.argmax(), temp.shape)
    # Set center's indices:
    start_row = idx[0] + row_lower
    start_col = idx[1] + col_lower

  return [start_row, start_col]

'''
eat_carrots
<-Takes the input array, carrot counter, and current position of Bunny
->Recursively outputs the total number of carrots Bunny ate

Eat carrots depending on current location
'''
def eat_carrots(field, counter = 0, curr_position = []):
  # First call needs to set Bunny's starting position
  if not curr_position:
    curr_position = find_start(field)

  # Set values for current position and lengths
  i = curr_position[0]
  j = curr_position[1]
  row_length = len(field)
  col_length = len(field[0])

  # Eat carrots from current position
  counter += field[i][j]
  # Set current cell's carrot count to 0
  field[i][j] = 0

  # Set direction variables to -1 for max value determination
  north, south, east, west = -1, -1, -1, -1

  # Bounds check:
  if i-1 < row_length and i-1 >= 0:
    north = field[i-1][j]
  if i+1 < row_length and i+1 >= 0:
    south = field[i+1][j]
  if j+1 < col_length and j+1 >= 0:
    east = field[i][j+1]
  if j-1 < col_length and j-1 >= 0:
    west = field[i][j-1]

  # At this point, if any direction vars are -1, this means that direction is out of bounds

  # Map the possible directions' values to their locations on the field for easy access
  routes = {
    north:  [i-1, j],
    south:  [i+1, j],
    east:   [i, j+1],
    west:   [i, j-1]
  }

  # Find next cell to eat
  eat_next = max(routes)

  # Base case is when there are no carrots in the max adjacent cell
  if eat_next < 1:
    return counter
  else:
    # Recurse until all adjacent cells are empty
    return eat_carrots(field, counter, routes[eat_next])

if __name__ == '__main__':
  test.main()