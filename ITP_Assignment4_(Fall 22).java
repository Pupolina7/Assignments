import java.io.FileOutputStream;
import java.util.HashMap;
import java.util.Map;
import java.io.File;
import java.util.Scanner;

public final class Main {
    private Main() { };
    /**
     * declaring class "Board" to work with chess figures.
     */
    private static Board chessBoard;
    /**
     * Our main method of the code.
     * @param args The command line argument.
     */
    public static void main(String[] args) {
        //using try-catch blocks for handling exceptions.
        //declaring "output.txt" as output stream.
        try (FileOutputStream outputStream = new FileOutputStream("output.txt")) {
        try {
            //declaring "input.txt" file.
            File input = new File("input.txt");
            //declaring scanner to work with data from input file.
            Scanner scanner = new Scanner(input);
            //local variables n, m for board size and number of chess pieces respectively.
            int n;
            int m;
            //scanning the board size from input file.
            n = scanner.nextInt();
            //declaring maximal board size.
            final int maxN = 1000;
            //declaring minimal board size.
            final int minN = 3;
            //declaring minimal number of chess figures.
            final int minM = 2;
            //checking if the board size satisfies given conditions.
            if (n > maxN || n < minN) {
                throw new InvalidBoardSizeException();
            }
            //scanning the number of chess figures.
            m = scanner.nextInt();
            //checking if the number of pieces satisfies given condition.
            if (m < minM || m > (n * n)) {
                throw new InvalidNumberOfPiecesException();
            }
            //assigning to variable chessBoard new board with given size (n).
            chessBoard = new Board(n);
            //declaring variables to count white and black kings.
            int whiteKing = 0;
            int blackKing = 0;
            //creating an array of m strings to collect input figures positions.
            String[] figures = new String[m];
            //declaring variable j to fill an array.
            int j = 0;
            //using for-loop to scan input figures.
            for (int i = 0; i < m; i++) {
                //scanning figure.
                String pieceType = scanner.next();
                //declaring variable chessPiece to use it for declaring figures (inheritance).
                ChessPiece chessPiece;
                //scanning color.
                String color = scanner.next();
                //converting string with color into enum type "PieceColor".
                PieceColor pieceColor = PieceColor.parse(color);
                //scanning and converting pieces position into integers.
                int x = Integer.parseInt(scanner.next());
                int y = Integer.parseInt(scanner.next());
                //assigning piece position for current figure.
                PiecePosition piecePosition = new PiecePosition(x, y);
                //checking if coordinates of the figure satisfy board size.
                if (x < 1 || x > n || y < 1 || y > n) {
                    throw new InvalidPiecePositionException();
                }
                //using "switch" to determine piece type and assign it to chessPiece.
                switch (pieceType) {
                    case "Pawn":
                        chessPiece = new Pawn(piecePosition, pieceColor);
                        break;
                    case "Bishop":
                        chessPiece = new Bishop(piecePosition, pieceColor);
                        break;
                    case "Knight":
                        chessPiece = new Knight(piecePosition, pieceColor);
                        break;
                    case "Rook":
                        chessPiece = new Rook(piecePosition, pieceColor);
                        break;
                    case "Queen":
                        chessPiece = new Queen(piecePosition, pieceColor);
                        break;
                    case "King":
                        //counting black and white kings.
                        chessPiece = new King(piecePosition, pieceColor);
                        if (chessPiece.color == PieceColor.WHITE) {
                            whiteKing++;
                        } else if (chessPiece.color == PieceColor.BLACK) {
                            blackKing++;
                        }
                        break;
                        //throwing exception if input piece type does not satisfy given conditions.
                    default:
                        throw new InvalidPieceNameException();
                }
                //throwing exception if no color was entered.
                if (pieceColor == null) {
                    throw new InvalidPieceColorException();
                }
                //adding current piece to the array of figures.
                figures[j] = chessPiece.position.toString();
                //adding chess piece on the board.
                chessBoard.addPiece(chessPiece);
                j++;
                //checking if file contains less that m figures.
                if (i == (m - 2) && !(scanner.hasNext())) {
                    throw new InvalidNumberOfPiecesException();
                }
            }
            //if file has more than m figures throwing exception.
            if (scanner.hasNext()) {
                throw new InvalidNumberOfPiecesException();
            }
            //if there are not exactly one black and white king throwing exception.
            if (whiteKing != 1 || blackKing != 1) {
                throw new InvalidGivenKingsException();
            }
            if (j != m) {
                throw new InvalidNumberOfPiecesException();
            }
            //using for-loop to output number of moves and captures for every piece.
            for (int i = 0; i < m; i++) {
                int moves = chessBoard.getPiecePossibleMovesCount(chessBoard.getPiece(figures[i]));
                int captures = chessBoard.getPiecePossibleCapturesCount(chessBoard.getPiece(figures[i]));
                //declaring the string containing number of possible moves and captures foe output.
                String outputString = moves + " " + captures + "\n";
                byte[] output = outputString.getBytes();
                outputStream.write(output);
            }
            //using catch-blocks to handle exceptions.
        } catch (InvalidBoardSizeException e) {
            outputStream.write(e.getMessage().getBytes());
        } catch (InvalidNumberOfPiecesException e) {
            outputStream.write(e.getMessage().getBytes());
        } catch (InvalidPieceNameException e) {
            outputStream.write(e.getMessage().getBytes());
        } catch (InvalidPieceColorException e) {
            outputStream.write(e.getMessage().getBytes());
        } catch (InvalidPiecePositionException e) {
            outputStream.write(e.getMessage().getBytes());
        } catch (InvalidGivenKingsException e) {
            outputStream.write(e.getMessage().getBytes());
        } catch (java.lang.Exception e) {
            outputStream.write(new InvalidInputException().getMessage().getBytes());
        }
    } catch (java.lang.Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
/**
 * enumeration containing possible colors.
 * it has method "parse" that converts string into PieceColor type.
 */
enum PieceColor {
    /**
     * white figure color.
     */
    WHITE,
    /**
     * black figure color.
     */
    BLACK;

    /**
     * this method converts string into PieceColor (enumeration type).
     * @param string - string containing figures color.
     * @return PieceColor (enumeration type).
     */
    public static PieceColor parse(String string) {
        if (string.equals("White")) {
            return PieceColor.WHITE;
        } else if (string.equals("Black")) {
            return PieceColor.BLACK;
        } else {
            //returning "null" if color is neither white nor black.
            return null;
        }
    }
}
/**
 * Parent-class Exception.
 */
class Exception extends java.lang.Exception {
    public String getMessage() {
        return "Error\n";
    }
}
/**
 * this class is used to detect invalid board size.
 */
class InvalidBoardSizeException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid board size.
     */
    @Override
    public String getMessage() {
        return "Invalid board size\n";
    }
}
/**
 * this class is used to detect invalid number of pieces.
 */
class InvalidNumberOfPiecesException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid number of pieces.
     */
    @Override
    public String getMessage() {
        return "Invalid number of pieces\n";
    }
}
/**
 * this class is used to detect invalid figures names.
 */
class InvalidPieceNameException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid piece name.
     */
    @Override
    public String getMessage() {
        return "Invalid piece name\n";
    }
}
/**
 * this class is used to detect invalid figures color.
 */
class InvalidPieceColorException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid piece color.
     */
    @Override
    public String getMessage() {
        return "Invalid piece color\n";
    }
}
/**
 * this class is used to detect invalid position.
 */
class InvalidPiecePositionException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid piece position.
     */
    @Override
    public String getMessage() {
        return "Invalid piece position\n";
    }
}
/**
 * this class is used to detect invalid number of kings.
 */
class InvalidGivenKingsException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid given Kings.
     */
    @Override
    public String getMessage() {
        return "Invalid given Kings\n";
    }
}
/**
 * this class is used to detect other invalid inputs.
 */
class InvalidInputException extends Exception {
    /**
     * this method outputs exception message.
     * @return message: Invalid input.
     */
    @Override
    public String getMessage() {
        return "Invalid input\n";
    }
}
/**
 * this class is used to work with pieces positions.
 */
class PiecePosition {
    /**
     * private variable x to save "x-coordinate" of pieces position.
     */
    private final int x;
    /**
     * private variable y to save "y-coordinate" of pieces position.
     */
    private final int y;
    /**
     * public class to assign private variables x and y.
     * @param onX - "x-coordinate" of pieces position.
     * @param onY - "y-coordinate" of pieces position.
     */
    PiecePosition(int onX, int onY) {
        this.x = onX;
        this.y = onY;
    }
    /**
     * method is used to get "x-coordinate" of pieces position.
     * @return "x-coordinate" of pieces position.
     */
    public int getX() {
        return x;
    }
    /**
     * method is used to get "y-coordinate" of pieces position.
     * @return "y-coordinate" of pieces position.
     */
    public int getY() {
        return y;
    }
    /**
     * this method converts pieces coordinates into "key" string to later associate figures with it.
     * @return string containing pieces position.
     */
    public String toString() {
        return x + " " + y;
    }
}
/**
 * abstract class to implement common for all figures characteristics.
 */
abstract class ChessPiece {
    /**
     * protected variable to store pieces color.
     */
    protected PieceColor color;
    /**
     * protected variable to store pieces position.
     */
    protected PiecePosition position;
    /**
     * public class to assign pieces position and color.
     * @param piecePosition - pieces position (x, y).
     * @param pieceColor - pieces color (white/black).
     */
    ChessPiece(PiecePosition piecePosition, PieceColor pieceColor) {
        this.position = piecePosition;
        this.color = pieceColor;
    }
    /**
     * method is used to get pieces position.
     * @return - pieces position (x, y).
     */
    public PiecePosition getPosition() {
        return position;
    }
    /**
     * method is used to get pieces color.
     * @return - pieces color.
     */
    public PieceColor getColor() {
        return color;
    }
    /**
     * abstract method is used to get number of pieces moves.
     * @param positions - map containing key: string with pieces position (x y).
     * @param boardSize - board size n.
     * @return - number of pieces moves.
     */
    public abstract int getMovesCount(Map<String, ChessPiece> positions, int boardSize);
    /**
     * abstract method is used to get number of pieces captures.
     * @param positions - map containing key: string with pieces position (x y).
     * @param boardSize - board size n.
     * @return - number of pieces captures.
     */
    public abstract int getCapturesCount(Map<String, ChessPiece> positions, int boardSize);
}
/**
 * child-class to implement Knights actions.
 */
class Knight extends ChessPiece {
    /**
     * this method is used to assign current pieces position and color to the super-class.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     */
    Knight(PiecePosition position, PieceColor color) {
        super(position, color);
    }
    /**
     * this method implements Knights moves.
     * it implements each possible move in separate loop.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Knights possible moves.
     */
    @Override
    public int getMovesCount(Map<String, ChessPiece> positions, int boardSize) {
        //declaring local variable to count moves.
        int moves = 0;
        //checking if pieces position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1 && position.getY() <= boardSize
                && position.getY() >= 1) {
            //check if pieces position still satisfies board size after movement.
            if (position.getX() + 2 <= boardSize && position.getY() + 1 <= boardSize) {
                //checking if the place where figure tries to move contains other figure.
                if (positions.containsKey(new PiecePosition(position.getX() + 2, position.getY()
                        + 1).toString())) {
                    //if the place where figure tries to move contains other figure, checking that this figure has
                    //different color, so, it will be capture.
                    if (positions.get(new PiecePosition(position.getX() + 2, position.getY()
                            + 1).toString()).getColor() != color) {
                        //counting this move.
                        moves++;
                    }
                } else {
                    //if the position where figure tried to move was empty, counting it too.
                    moves++;
                }
            }
            //using the same approach implementing this procedure for all other possible Knights moves.
            if (position.getX() + 2 <= boardSize && position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() + 2, position.getY()
                        - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 2, position.getY()
                            - 1).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
            if (position.getX() + 1 <= boardSize && position.getY() + 2 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                        + 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                            + 2).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
            if (position.getX() - 1 >= 1 && position.getY() + 2 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                        + 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                            + 2).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
            if (position.getX() - 2 >= 1 && position.getY() + 1 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() - 2, position.getY()
                        + 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 2, position.getY()
                            + 1).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
            if (position.getX() - 2 >= 1 && position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() - 2, position.getY()
                        - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 2, position.getY()
                            - 1).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
            if (position.getX() - 1 >= 1 && position.getY() - 2 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                        - 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                            - 2).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
            if (position.getX() + 1 <= boardSize && position.getY() - 2 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                        - 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                            - 2).toString()).getColor() != color) {
                        moves++;
                    }
                } else {
                    moves++;
                }
            }
        }
        //returning number of all possible moves.
        return moves;
    }
    /**
     * this method implements Knights captures.
     * it implements each possible capture in separate loop.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Knights possible captures.
     */
    @Override
    public int getCapturesCount(Map<String, ChessPiece> positions, int boardSize) {
        //declaring local variable to count captures.
        int captures = 0;
        //checking if current position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1 && position.getY() <= boardSize
                && position.getY() >= 1) {
            //checking if the position still satisfies board size after movement.
            if (position.getX() + 2 <= boardSize && position.getY() + 1 <= boardSize) {
                //checking if the position where figure tries to move contains other figure.
                if (positions.containsKey(new PiecePosition(position.getX() + 2, position.getY()
                        + 1).toString())) {
                    //checking if the position where figure tries to move contains figure of other color.
                    if (positions.get(new PiecePosition(position.getX() + 2, position.getY()
                            + 1).toString()).getColor() != color) {
                        //if all conditions where true adding this move as a capture.
                        captures++;
                    }
                }
            }
            //using the same approach implementing captures for moves in all other possible directions.
            if (position.getX() + 2 <= boardSize && position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() + 2, position.getY()
                        - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 2, position.getY()
                            - 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() + 1 <= boardSize && position.getY() + 2 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                        + 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                            + 2).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 1 >= 1 && position.getY() + 2 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                        + 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                            + 2).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 2 >= 1 && position.getY() + 1 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() - 2, position.getY()
                        + 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 2, position.getY()
                            + 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 2 >= 1 && position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() - 2, position.getY()
                        - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 2, position.getY()
                            - 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 1 >= 1 && position.getY() - 2 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                        - 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                            - 2).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() + 1 <= boardSize && position.getY() - 2 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                        - 2).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                            - 2).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
        }
        //returning number of all possible captures.
        return captures;
    }
}
//other figures classes use the same approach for implementing moves and captures.
/**
 * child-class to implement Kings actions.
 */
class King extends ChessPiece {
    /**
     * this method is used to assign current pieces position and color to the super-class.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     */
    King(PiecePosition position, PieceColor color) {
        super(position, color);
    }
    /**
     * this method implements Kings moves.
     * it implements each possible move in separate loop.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Kings possible moves.
     */
    @Override
    public int getMovesCount(Map<String, ChessPiece> positions, int boardSize) {
            int moves = 0;
            if (position.getX() <= boardSize && position.getX() >= 1 && position.getY() <= boardSize
                    && position.getY() >= 1) {
                if (position.getY() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX(), position.getY()
                            + 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX(), position.getY()
                                + 1).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getX() + 1 <= boardSize && position.getY() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                            + 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                                + 1).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getX() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() + 1,
                            position.getY()).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + 1,
                                position.getY()).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getX() + 1 <= boardSize && position.getY() - 1 >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                            - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                                - 1).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getY() - 1 >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX(),
                            position.getY() - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX(),
                                position.getY() - 1).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getX() - 1 >= 1 && position.getY() - 1 >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                            - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                                - 1).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getX() - 1 >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1,
                            position.getY()).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1,
                                position.getY()).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
                if (position.getX() - 1 >= 1 && position.getY() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                            + 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                                + 1).toString()).getColor() != color) {
                            moves++;
                        }
                    } else {
                        moves++;
                    }
                }
            }
            return moves;
        }
    /**
     * this method implements Kings captures.
     * it implements each possible capture in separate loop.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Kings possible captures.
     */
    @Override
    public int getCapturesCount(Map<String, ChessPiece> positions, int boardSize) {
        int captures = 0;
        if (position.getX() <= boardSize && position.getX() >= 1 && position.getY() <= boardSize
                && position.getY() >= 1) {
            if (position.getY() + 1 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX(), position.getY()
                        + 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX(), position.getY()
                            + 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() + 1 <= boardSize && position.getY() + 1 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                        + 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                            + 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() + 1 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1,
                        position.getY()).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1,
                            position.getY()).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() + 1 <= boardSize && position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() + 1, position.getY()
                        - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() + 1, position.getY()
                            - 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX(),
                        position.getY() - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX(),
                            position.getY() - 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 1 >= 1 && position.getY() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                        - 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                            - 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 1 >= 1) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1,
                        position.getY()).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1,
                            position.getY()).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
            if (position.getX() - 1 >= 1 && position.getY() + 1 <= boardSize) {
                if (positions.containsKey(new PiecePosition(position.getX() - 1, position.getY()
                        + 1).toString())) {
                    if (positions.get(new PiecePosition(position.getX() - 1, position.getY()
                            + 1).toString()).getColor() != color) {
                        captures++;
                    }
                }
            }
        }
        return captures;
    }
}
/**
 * child-class to implement Pawns actions.
 */
class Pawn extends ChessPiece {
    /**
     * this method is used to assign current pieces position and color to the super-class.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     */
    Pawn(PiecePosition position, PieceColor color) {
        super(position, color);
    }
    /**
     * this method implements Pawns moves.
     * it implements each possible move in separate loop.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Pawns possible moves.
     */
    @Override
    public int getMovesCount(Map<String, ChessPiece> positions, int boardSize) {
        int moves = 0;
        if (position.getX() <= boardSize && position.getX() >= 1
        && position.getY() <= boardSize && position.getY() >= 1) {
            //if the Pawn is white, implementing its possible moves.
            if (color == PieceColor.WHITE) {
                //check if pieces position still satisfies board size after movement.
                if (position.getY() + 1 <= boardSize) {
                    if (!positions.containsKey(new PiecePosition(position.getX(), position.getY()
                            + 1).toString())) {
                        moves++;
                    }
                }
                //using the same approach implementing this procedure for all other possible Pawns moves.
                if (position.getX() + 1 <= boardSize && position.getY() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() + 1,
                            position.getY() + 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + 1,
                                position.getY() + 1).toString()).getColor() != color) {
                            moves++;
                        }
                    }
                }
                if (position.getX() - 1 >= 1 && position.getY() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1,
                            position.getY() + 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1,
                                position.getY() + 1).toString()).getColor() != color) {
                            moves++;
                        }
                    }
                }
                //if the Pawn is black, implementing its possible moves.
            } else if (color == PieceColor.BLACK) {
                if (position.getY() - 1 >= 1) {
                    if (!positions.containsKey(new PiecePosition(position.getX(), position.getY()
                            - 1).toString())) {
                        moves++;
                    }
                }
                if (position.getY() - 1 >= 1 && position.getX() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() + 1,
                            position.getY() - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + 1,
                                position.getY() - 1).toString()).getColor() != color) {
                            moves++;
                        }
                    }
                }
                if (position.getY() - 1 >= 1 && position.getX() - 1 >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1,
                            position.getY() - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1,
                                position.getY() - 1).toString()).getColor() != color) {
                            moves++;
                        }
                    }
                }
            }
        }
        //returning number of all possible moves.
        return moves;
    }
    /**
     * this method implements Pawns captures.
     * it implements each possible capture in separate loop.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Pawns possible captures.
     */
    @Override
    public int getCapturesCount(Map<String, ChessPiece> positions, int boardSize) {
        //declaring local variable to count captures.
        int captures = 0;
        //checking if pieces position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1
                && position.getY() <= boardSize && position.getY() >= 1) {
            //if the Pawn is white, implementing its possible captures (they are differ from moves).
            if (color == PieceColor.WHITE) {
                //check if pieces position still satisfies board size after movement.
                if (position.getX() + 1 <= boardSize && position.getY() + 1 <= boardSize) {
                    //checking if the place where figure tries to move contains other figure.
                    if (positions.containsKey(new PiecePosition(position.getX() + 1,
                            position.getY() + 1).toString())) {
                        //checking if the position where figure tries to move contains figure of other color.
                        if (positions.get(new PiecePosition(position.getX() + 1,
                                position.getY() + 1).toString()).getColor() != color) {
                            //if all conditions where true adding this move as a capture.
                            captures++;
                        }
                    }
                }
                //using the same approach implementing captures for moves in all other possible directions.
                if (position.getX() - 1 >= 1 && position.getY() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1,
                            position.getY() + 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1,
                                position.getY() + 1).toString()).getColor() != color) {
                            captures++;
                        }
                    }
                }
                //if the Pawn is black, implementing its possible captures (they are differ from moves).
            } else if (color == PieceColor.BLACK) {
                if (position.getY() - 1 >= 1 && position.getX() + 1 <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() + 1,
                            position.getY() - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + 1,
                                position.getY() - 1).toString()).getColor() != color) {
                            captures++;
                        }
                    }
                }
                if (position.getY() - 1 >= 1 && position.getX() - 1 >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() - 1,
                            position.getY() - 1).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - 1,
                                position.getY() - 1).toString()).getColor() != color) {
                            captures++;
                        }
                    }
                }
            }
        }
        //returning number of all possible captures.
        return captures;
    }
}
/**
 * child-class to implement Bishops actions.
 */
class Bishop extends ChessPiece implements BishopMovement {
    /**
     * this method is used to assign current pieces position and color to the super-class.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     */
    Bishop(PiecePosition position, PieceColor color) {
        super(position, color);
    }
    /**
     * this method is used to count Bishops possible moves, using getDiagonalMovesCount method.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Bishops possible moves.
     */
    @Override
    public int getMovesCount(Map<String, ChessPiece> positions, int boardSize) {
        return getDiagonalMovesCount(position, color, positions, boardSize);
    }
    /**
     * this method is used to count Bishops possible captures, using getDiagonalCapturesCount method.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Bishops possible captures.
     */
    @Override
    public int getCapturesCount(Map<String, ChessPiece> positions, int boardSize) {
        return getDiagonalCapturesCount(position, color, positions, boardSize);
    }
}
/**
 * child-class to implement Rooks actions.
 */
class Rook extends ChessPiece implements RookMovement {
    /**
     * this method is used to assign current pieces position and color to the super-class.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     */
    Rook(PiecePosition position, PieceColor color) {
        super(position, color);
    }
    /**
     * this method is used to count Rooks possible moves, using getOrthogonalMovesCount method.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Rooks possible moves.
     */
    @Override
    public int getMovesCount(Map<String, ChessPiece> positions, int boardSize) {
        return getOrthogonalMovesCount(position, color, positions, boardSize);
    }
    /**
     * this method is used to count Rooks possible captures, using getOrthogonalCapturesCount method.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Rooks possible captures.
     */
    @Override
    public int getCapturesCount(Map<String, ChessPiece> positions, int boardSize) {
        return getOrthogonalCapturesCount(position, color, positions, boardSize);
    }

}
/**
 * child-class to implement Queens actions.
 */
class Queen extends ChessPiece implements BishopMovement, RookMovement {
    /**
     * this method is used to assign current pieces position and color to the super-class.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     */
    Queen(PiecePosition position, PieceColor color) {
        super(position, color);
    }
    /**
     * this method is used to count Queens possible moves, using getDiagonalsMovesCount and
     * getOrthogonalMovesCount methods.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Queens possible moves.
     */
    @Override
    public int getMovesCount(Map<String, ChessPiece> positions, int boardSize) {
        return getOrthogonalMovesCount(position, color, positions, boardSize)
                + getDiagonalMovesCount(position, color, positions, boardSize);
    }
    /**
     * this method is used to count Queens possible captures, using getDiagonalsCapturesCount and
     * getOrthogonalCapturesCount methods.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size n.
     * @return number of Queens possible captures.
     */
    @Override
    public int getCapturesCount(Map<String, ChessPiece> positions, int boardSize) {
        return getDiagonalCapturesCount(position, color, positions, boardSize)
                + getOrthogonalCapturesCount(position, color, positions, boardSize);
    }
}

/**
 * this class is used to work with figures on the board.
 */
class Board {
    /**
     * this map is used to make an "association" between figures position and type.
     */
    private final Map<String, ChessPiece> positionsToPieces = new HashMap<>();
    /**
     * private variable to store current board size.
     */
    private final int size;
    /**
     * this method is used to assign private size of that class.
     * @param boardSize - current board size.
     */
    Board(int boardSize) {
        this.size = boardSize;
    }

    /**
     * this method is used to get the number of pieces possible moves.
     * @param piece - figure.
     * @return number of pieces possible moves.
     */
    public int getPiecePossibleMovesCount(ChessPiece piece) {
        return piece.getMovesCount(positionsToPieces, size);
    }
    /**
     * this method is used to get the number of pieces possible captures.
     * @param piece - figure.
     * @return number of pieces possible captures.
     */
    public int getPiecePossibleCapturesCount(ChessPiece piece) {
        return piece.getCapturesCount(positionsToPieces, size);
    }
    /**
     * this method is used to add figure on the board.
     * @param piece - figure.
     */
    public void addPiece(ChessPiece piece) {
        positionsToPieces.put(piece.getPosition().toString(), piece);
    }
    /**
     * this method is used to get figure on the given position.
     * @param position - string containing figures position.
     * @return figure on a given position.
     */
    public ChessPiece getPiece(String position) {
       return positionsToPieces.get(position);
    }
}
interface BishopMovement {
    /**
     * this method is used to implement Bishop (diagonal) Movement.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size (n).
     * @return number of all possible diagonal moves.
     */
    default int getDiagonalMovesCount(PiecePosition position, PieceColor color, Map<String, ChessPiece> positions,
                                      int boardSize) {
        //declaring local variable to count moves.
        int moves = 0;
        //checking if pieces position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1
        && position.getY() <= boardSize && position.getY() >= 1) {
            //using for-loop to implement movements on the same diagonal.
            for (int i = 1; i <= boardSize; i++) {
                //check if pieces position still satisfies board size after movement.
                if (position.getX() + i <= boardSize && position.getY() + i <= boardSize) {
                    //checking if the place where figure tries to move contains other figure.
                    if (positions.containsKey(new PiecePosition(position.getX() + i,
                            position.getY() + i).toString())) {
                        //if the place where figure tries to move contains other figure, checking that this figure has
                        //different color, so, it will be capture.
                        if (positions.get(new PiecePosition(position.getX() + i,
                                position.getY() + i).toString()).getColor() != color) {
                            //counting this move.
                            moves++;
                        }
                        //breaking loop if the position contains figure, as we cannot go over it.
                        break;
                    } else {
                        //if the position where figure tried to move was empty, counting it too.
                        moves++;
                    }
                } else {
                    //breaking the loop if we reached the end of the board.
                    break;
                }
            }
            //using the same approach implementing this procedure for all other possible diagonal moves.
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() + i <= boardSize && position.getY() - i >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() + i,
                            position.getY() - i).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + i,
                                position.getY() - i).toString()).getColor() != color) {
                            moves++;
                        }
                        break;
                    } else {
                        moves++;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() - i >= 1 && position.getY() + i <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - i,
                            position.getY() + i).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - i,
                                position.getY() + i).toString()).getColor() != color) {
                            moves++;
                        }
                        break;
                    } else {
                        moves++;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() - i >= 1 && position.getY() - i >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() - i,
                            position.getY() - i).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - i,
                                position.getY() - i).toString()).getColor() != color) {
                            moves++;
                        }
                        break;
                    } else {
                        moves++;
                    }
                } else {
                    break;
                }
            }
        }
        //returning number of all possible moves.
        return moves;
    }
    /**
     * this method is used to implement Bishop (diagonal) Captures.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size (n).
     * @return number of all possible diagonal captures.
     */
    default int getDiagonalCapturesCount(PiecePosition position, PieceColor color, Map<String, ChessPiece> positions,
                                        int boardSize) {
        //declaring local variable to count captures.
        int captures = 0;
        //checking if pieces position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1
                && position.getY() <= boardSize && position.getY() >= 1) {
            //using for-loop to implement movements on the same diagonal.
            for (int i = 1; i <= boardSize; i++) {
                //check if pieces position still satisfies board size after movement.
                if (position.getX() + i <= boardSize && position.getY() + i <= boardSize) {
                    //checking if the place where figure tries to move contains other figure.
                    if (positions.containsKey(new PiecePosition(position.getX() + i,
                            position.getY() + i).toString())) {
                        //checking if the position where figure tries to move contains figure of other color.
                        if (positions.get(new PiecePosition(position.getX() + i,
                                position.getY() + i).toString()).getColor() != color) {
                            //if all conditions where true adding this move as a capture.
                            captures++;
                        }
                        //breaking loop if the position contains figure, as we cannot go over it.
                        break;
                    }
                } else {
                    //breaking the loop if we reached the end of the board.
                    break;
                }
            }
            //using the same approach implementing captures for moves in all other possible directions.
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() + i <= boardSize && position.getY() - i >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() + i,
                            position.getY() - i).toString())) {
                        if (positions.get(new PiecePosition(position.getX() + i,
                                position.getY() - i).toString()).getColor() != color) {
                            captures++;
                        }
                        break;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() - i >= 1 && position.getY() + i <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - i,
                            position.getY() + i).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - i,
                                position.getY() + i).toString()).getColor() != color) {
                            captures++;
                        }
                        break;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() - i >= 1 && position.getY() - i >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX() - i,
                            position.getY() - i).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - i,
                                position.getY() - i).toString()).getColor() != color) {
                            captures++;
                        }
                        break;
                    }
                } else {
                    break;
                }
            }
        }
        //returning number of all possible captures.
        return captures;
    }
}
interface RookMovement {
    /**
     * this method is used to implement Rook (orthogonal) Movement.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size (n).
     * @return number of all possible orthogonal moves.
     */
    default int getOrthogonalMovesCount(PiecePosition position, PieceColor color, Map<String, ChessPiece> positions,
                                       int boardSize) {
        //declaring local variable to count moves.
        int moves = 0;
        //checking if pieces position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1
                && position.getY() <= boardSize && position.getY() >= 1) {
            //using for-loop to implement movements on the same line.
            for (int i = 1; i < boardSize; i++) {
                //check if pieces position still satisfies board size after movement.
                if (position.getX() + i <= boardSize && position.getY() <= boardSize) {
                    //checking if the place where figure tries to move contains other figure.
                    if (positions.containsKey(new PiecePosition(position.getX() + i,
                            position.getY()).toString())) {
                        //if the place where figure tries to move contains other figure, checking that this figure has
                        //different color, so, it will be capture.
                        if (positions.get(new PiecePosition(position.getX() + i,
                                position.getY()).toString()).getColor() != color) {
                            //counting this move.
                            moves++;
                        }
                        //breaking loop if the position contains figure, as we cannot go over it.
                        break;
                    } else {
                        //if the position where figure tried to move was empty, counting it too.
                        moves++;
                    }
                } else {
                    //breaking the loop if we reached the end of the board.
                    break;
                }
            }
            //using the same approach implementing this procedure for all other possible orthogonal moves.
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() - i >= 1 && position.getY() <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - i,
                            position.getY()).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - i,
                                position.getY()).toString()).getColor() != color) {
                            moves++;
                        }
                        break;
                    } else {
                        moves++;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() <= boardSize && position.getY() + i <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX(),
                            position.getY() + i).toString())) {
                        if (positions.get(new PiecePosition(position.getX(),
                                position.getY() + i).toString()).getColor() != color) {
                            moves++;
                        }
                        break;
                    } else {
                        moves++;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() <= boardSize && position.getY() - i >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX(),
                            position.getY() - i).toString())) {
                        if (positions.get(new PiecePosition(position.getX(),
                                position.getY() - i).toString()).getColor() != color) {
                            moves++;
                        }
                        break;
                    } else {
                        moves++;
                    }
                } else {
                    break;
                }
            }
        }
        //returning number of all possible moves.
        return moves;
    }
    /**
     * this method is used to implement Rook (orthogonal) Captures.
     * @param position - pieces position (x, y).
     * @param color - pieces color.
     * @param positions - map containing key: string with pieces position (x y) and figure type.
     * @param boardSize - board size (n).
     * @return number of all possible orthogonal captures.
     */
    default int getOrthogonalCapturesCount(PiecePosition position, PieceColor color, Map<String, ChessPiece> positions,
                                          int boardSize) {
        //declaring local variable to count captures.
        int captures = 0;
        //checking if pieces position satisfies board size.
        if (position.getX() <= boardSize && position.getX() >= 1
                && position.getY() <= boardSize && position.getY() >= 1) {
            //using for-loop to implement movements on the same line.
            for (int i = 1; i <= boardSize; i++) {
                //check if pieces position still satisfies board size after movement.
                if (position.getX() + i <= boardSize && position.getY() <= boardSize) {
                    //checking if the place where figure tries to move contains other figure.
                    if (positions.containsKey(new PiecePosition(position.getX() + i,
                            position.getY()).toString())) {
                        //checking if the position where figure tries to move contains figure of other color.
                        if (positions.get(new PiecePosition(position.getX() + i,
                                position.getY()).toString()).getColor() != color) {
                            //if all conditions where true adding this move as a capture.
                            captures++;
                        }
                        //breaking loop if the position contains figure, as we cannot go over it.
                        break;
                    }
                } else {
                    //breaking the loop if we reached the end of the board.
                    break;
                }
            }
            //using the same approach implementing captures for moves in all other possible directions.
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() - i >= 1 && position.getY() <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX() - i,
                            position.getY()).toString())) {
                        if (positions.get(new PiecePosition(position.getX() - i,
                                position.getY()).toString()).getColor() != color) {
                            captures++;
                        }
                        break;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() <= boardSize && position.getY() + i <= boardSize) {
                    if (positions.containsKey(new PiecePosition(position.getX(),
                            position.getY() + i).toString())) {
                        if (positions.get(new PiecePosition(position.getX(),
                                position.getY() + i).toString()).getColor() != color) {
                            captures++;
                        }
                        break;
                    }
                } else {
                    break;
                }
            }
            for (int i = 1; i <= boardSize; i++) {
                if (position.getX() <= boardSize && position.getY() - i >= 1) {
                    if (positions.containsKey(new PiecePosition(position.getX(),
                            position.getY() - i).toString())) {
                        if (positions.get(new PiecePosition(position.getX(),
                                position.getY() - i).toString()).getColor() != color) {
                            captures++;
                        }
                        break;
                    }
                } else {
                    break;
                }
            }
        }
        //returning number of all possible captures.
        return captures;
    }
}
