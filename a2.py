# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    def __init__(self, symbol, row, col):
        """ (Rat, str,int,int)-> Nonetype
The first parameter represents the rat to be initialized, the second parameter represents the 1-character symbol for the rat, the third parameter represents the row where the rat is located, and the fourth parameter represents the column where the rat is located.
>>> R=Rat('P',1,4)
>>> R.symbol
'P'
"""
        self.symbol=symbol
        self.row=row
        self.col=col
        self.num_sprouts_eaten=0
        
    """ A rat caught in a maze. """
    def set_location(self,row,col):
        """(Rat,int,int)->NoneType
The first parameter represents a rat, the second represents a row, and the third represents a column. Set the rat's row and col instance variables to the given row and column.
set_location(3,5)
R.row=3
"""
        
        self.row=row
        self.col=col
    def eat_sprout(self):
        """(Rat)->NoneType
The first parameter represents a rat. Add one to the rat's instance variable num_sprouts_eaten. Yuck
>>> R=Rat('P',1,4)
>>> R.eat_sprout()
>>> R.num_sprouts_eaten
1
"""
        self.num_sprouts_eaten+=1
    def  __str__(self):
        """ (Rat)->NoneType
The parameter represents a rat. Return a string representation of the rat, in this format:
>>> R=Rat('P',1,4)
>>> str(R) 
'P at (1,4) ate 0 sprouts.'
"""
        return self.symbol +" at "+"("+str(self.row)+","+str(self.col)+")"+ " ate "+ str(self.num_sprouts_eaten) +" sprouts."

    # Write your Rat methods here.

class Maze:
    def __init__(self,maze,rat_1,rat_2):
       """(Maze, list of list of str, Rat, Rat)->NoneType
The first paramter represents the maze to be initialized, the second parameter represents the contents of the maze, the third parameter represents the first rat in the maze, and the fourth parameter represents the second rat in the maze.
>>> M=Maze([['#', '#', '#', '#', '#', '#', '#'],\
      ['#', '.', '.', '.', '.', '.', '#'], \
      ['#', '.', '#', '#', '#', '.', '#'], \
      ['#', '.', '.', '@', '#', '.', '#'], \
      ['#', '@', '#', '.', '@', '.', '#'], \
      ['#', '#', '#', '#', '#', '#', '#']], \
      Rat('J', 1, 1),\
      Rat('P', 1, 4))
>>> M.maze
[['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
"""
       self.maze=maze
       self.rat_1=rat_1
       self.rat_2=rat_2
       self.num_sprouts_left=0
    """ A 2D maze. """
    def is_wall(self,row,col):
        """ (Maze,int,int)->bool

The first parameter represents a maze, the second represents a row, and the third represents a column.

Return True if and only if there is a wall at the given row and column of the maze.
>>> M=Maze([['#', '#', '#', '#', '#', '#', '#'],\
      ['#', '.', '.', '.', '.', '.', '#'], \
      ['#', '.', '#', '#', '#', '.', '#'], \
      ['#', '.', '.', '@', '#', '.', '#'], \
      ['#', '@', '#', '.', '@', '.', '#'], \
      ['#', '#', '#', '#', '#', '#', '#']], \
      Rat('J', 1, 1),\
      Rat('P', 1, 4))
>>> M.is_wall(0,0)
True
>>> M.maze[0][0]=="#"
True
"""
        return self.maze[row][col]==WALL
    def get_character(self,row,col):
        """ (Maze, int, int)->str
The first parameter represents a maze, the second represents a row, and the third represents a column.

Return the character in the maze at the given row and column. If there is a rat at that location, then its character should be returned rather than HALL.
>>> M=Maze([['#', '#', '#', '#', '#', '#', '#'],\
      ['#', '.', '.', '.', '.', '.', '#'], \
      ['#', '.', '#', '#', '#', '.', '#'], \
      ['#', '.', '.', '@', '#', '.', '#'], \
      ['#', '@', '#', '.', '@', '.', '#'], \
      ['#', '#', '#', '#', '#', '#', '#']], \
      Rat('J', 1, 1),\
      Rat('P', 1, 4))
>>> M.get_character(0,0)
'#'
>>> M.get_character(1,1)
'J'

"""
        if (self.rat_1.row , self.rat_1.col)==(row,col):
            return self.rat_1.symbol
        elif (self.rat_2.row , self.rat_2.col)==(row,col):
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self,rat,V_dir_change,H_dir_change):
        """(Maze, Rat, int, int)->bool
The first parameter represents a maze, the second represents a rat, the third represents a vertical direction change (UP, NO_CHANGE or DOWN), and the fourth represents a horizontal direction change (LEFT, NO_CHANGE or RIGHT).

Move the rat in the given direction, unless there is a wall in the way. Also, check for a Brussels sprout at that location and, if present:
>>> M=Maze([['#', '#', '#', '#', '#', '#', '#'],\
      ['#', '.', '.', '.', '.', '.', '#'], \
      ['#', '.', '#', '#', '#', '.', '#'], \
      ['#', '.', '.', '@', '#', '.', '#'], \
      ['#', '@', '#', '.', '@', '.', '#'], \
      ['#', '#', '#', '#', '#', '#', '#']], \
      Rat('J', 1, 1),\
      Rat('P', 1, 4))

"""
            
        if not self.is_wall(rat.row,rat.col):
                
            if self.maze[rat.row][rat.col]==SPROUT:
                self.maze[rat.row][rat.col]=HALL
                rat.eat_sprout()
            
            rat.row+=V_dir_change
            rat.col+=H_dir_change
             
        else:
            return True


    def __str__(self):
            
        """(Rate)->str
The parameter represents a maze. Return a string representation of the maze, using the format shown in this example:
>>> M=Maze([['#', '#', '#', '#', '#', '#', '#'],\
      ['#', '.', '.', '.', '.', '.', '#'], \
      ['#', '.', '#', '#', '#', '.', '#'], \
      ['#', '.', '.', '@', '#', '.', '#'], \
      ['#', '@', '#', '.', '@', '.', '#'], \
      ['#', '#', '#', '#', '#', '#', '#']], \
      Rat('J', 1, 1),\
      Rat('P', 1, 4))
>>> str(M)
'J at (1,1) ate 0 sprouts.\nP at (1,4) ate 0 sprouts.'
"""
        return str(self.rat_1)+"\n"+str(self.rat_2)

if __name__=="__main__":
    
    import doctest
    doctest.testmod()
