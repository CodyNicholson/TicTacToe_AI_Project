from cell import Cell
from player import Player

class Board:

    def __init__(self):
        emptyCells:List[Cell]
        board:Player
        rootValues:List[Cell]
        initializeBoard()

    def initializeBoard(self):
        self.rootValues = []
        self.board = []
        
    def isRunning():
        if isWinning(Player.COMPUTER):
            return false
        if isWinning(Player.USER):
            return false
        if getEmptyCells().isEmpty():
            return false
        return true

    def isWinning(Player player):
        if ( board[0][0] == player && board[1][1] == player && board[2][2] == player ):
            return true
        if( board[0][2] == player && board[1][1] == player && board[2][0] == player ):
        	return true
        for (int i = 0; i < 3; i++):
        	# checking the rows
        	if ( board[i][0] == player && board[i][1] == player && board[i][2] == player ):
                return true

        	# checking the columns
        	if( board[0][i] == player && board[1][i] == player && board[2][i] == player ):
        		return true
        return false

    def getEmptyCells():
    	emptyCells = new ArrayList<>();
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == Player.NONE:
                    emptyCells.add(new Cell(i, j))
        return emptyCells

    def move(Cell point, Player player):
        board[point.getX()][point.getY()] = player 

    def getBestMove()
        int max = Integer.MIN_VALUE
        int best = Integer.MIN_VALUE
        for (int i = 0; i < rootValues.size(); ++i) { 
            if (max < rootValues.get(i).getMinimaxValue()) {
                max = rootValues.get(i).getMinimaxValue();
                best = i;
            }
        }

        return rootValues.get(best);
    }

    public void makeUserInput() {
        System.out.println("User's move: ");
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        Cell point = new Cell(x, y);
        move(point, Player.USER); 
    }

    public void displayBoard() {

    	System.out.println();
    	
        for (int i = 0; i < Constants.BOARD_SIZE; ++i) {
            for (int j = 0; j < Constants.BOARD_SIZE; ++j) {
                System.out.print(board[i][j] + " ");
            }
            
            System.out.println();
        }
    }

    public int returnMin(List<Integer> list) {
    	
        int min = Integer.MAX_VALUE;
        int index = Integer.MIN_VALUE;
        
        for (int i = 0; i < list.size(); ++i) {
            if (list.get(i) < min) {
                min = list.get(i);
                index = i;
            }
        }
        return list.get(index);
    }

    public int returnMax(List<Integer> list) {
        int max = Integer.MIN_VALUE;
        int index = Integer.MIN_VALUE;
        for (int i = 0; i < list.size(); ++i) {
            if (list.get(i) > max) {
                max = list.get(i);
                index = i;
            }
        }
        
        return list.get(index);
    }
 
    public void callMinimax(int depth, Player player){
        rootValues.clear();
        minimax(depth, player);
    }
    
    public int minimax(int depth, Player player) {

        if (isWinning(Player.COMPUTER)) return +1;
        if (isWinning(Player.USER)) return -1;

        List<Cell> availableCells = getEmptyCells();
        
        if (availableCells.isEmpty()) return 0; 

        List<Integer> scores = new ArrayList<>(); 

        for (int i = 0; i < availableCells.size(); i++) {
            
        	Cell point = availableCells.get(i);  

            if (player == Player.COMPUTER) { //X's turn select the highest from below minimax() call
                move(point, Player.COMPUTER); 
                int currentScore = minimax(depth + 1, Player.USER);
                scores.add(currentScore);

                if (depth == 0) {
                	point.setMinimaxValue(currentScore);
                    rootValues.add(point);
                }    	
                
            } else if (player == Player.USER) {//O's turn select the lowest from below minimax() call
                move(point, Player.USER); 
                scores.add(minimax(depth + 1, Player.COMPUTER));
            }
            
            board[point.getX()][point.getY()] = Player.NONE; //Reset this point
        }
        
        if( player == Player.COMPUTER ){
        	return returnMax(scores);
        }
        
        return returnMin(scores);
    }

	def getAvailablePoints():
		return emptyCells

	def setAvailablePoints(availablePoints):
		this.emptyCells = availablePoints
	
	def setupBoard():
		for i in range(0,3):
			for j in range(0,3):
				board[i][j] = Player.NONE
