import java.util.Scanner;
public class Main {
    /**
     * declaring a variable scanner for scanning input data.
     */
    private final Scanner scanner = new Scanner(System.in);
    /**
     * Our main method of the code.
     * @param args The command line argument.
     */
    public static void main(String[] args) {
        Main main = new Main();
        //reading calculator type from the first line of input using method readCalculator
        CalculatorType calculatorType = main.readCalculator();
        //checking if input argument satisfies condition (integer, double, string), using reportFatalError method
        //if it is not printing "Wrong calculator type"
        reportFatalError(calculatorType.name());
        //scanning the second line of input (total amount of commands) using readCommandsNumber method
        int numberOfOperations = main.readCommandsNumber();
        //outputting "Amount of commands is Not a Number" if number of operations does not satisfy given conditions
        if (numberOfOperations == 0) {
            System.out.println("Amount of commands is Not a Number");
            System.exit(0);
        }
        //scanning operation signs (using parseOperation method) and numbers
        //performing calculations for current type of operands
        for (int i = 0; i < numberOfOperations; i++) {
            //scanning operation sign using parseOperation method
            OperationType operation = main.parseOperation(main.scanner.next());
            //scanning operands from input
            String a = main.scanner.next();
            String b = main.scanner.next();
            //using "switch" looking for need calculator type
            switch (calculatorType) {
                case INTEGER:
                    IntegerCalculator integerCalculator = new IntegerCalculator();
                    //using "switch" looking for need operation for integers and performing it, outputting the result
                    switch (operation) {
                        case ADDITION:
                            System.out.println(integerCalculator.add(a, b));
                            break;
                        case SUBTRACTION:
                            System.out.println(integerCalculator.subtract(a, b));
                            break;
                        case MULTIPLICATION:
                            System.out.println(integerCalculator.multiply(a, b));
                            break;
                        case DIVISION:
                            System.out.println(integerCalculator.divide(a, b));
                            break;
                        default:
                            System.out.println("Wrong operation type");
                            break;
                    }
                    break;
                case DOUBLE:
                    DoubleCalculator doubleCalculator = new DoubleCalculator();
                    //using "switch" looking for need operation for doubles and performing it, outputting the result
                    switch (operation) {
                        case ADDITION:
                            System.out.println(doubleCalculator.add(a, b));
                            break;
                        case SUBTRACTION:
                            System.out.println(doubleCalculator.subtract(a, b));
                            break;
                        case MULTIPLICATION:
                            System.out.println(doubleCalculator.multiply(a, b));
                            break;
                        case DIVISION:
                            System.out.println(doubleCalculator.divide(a, b));
                            break;
                        default:
                            System.out.println("Wrong operation type");
                            break;
                    }
                    break;
                case STRING:
                    StringCalculator stringCalculator = new StringCalculator();
                    //using "switch" looking for need operation for strings and performing it, outputting the result
                    switch (operation) {
                        case ADDITION:
                            System.out.println(stringCalculator.add(a, b));
                            break;
                        case SUBTRACTION:
                            System.out.println(stringCalculator.subtract(a, b));
                            break;
                        case MULTIPLICATION:
                            System.out.println(stringCalculator.multiply(a, b));
                            break;
                        case DIVISION:
                            System.out.println(stringCalculator.divide(a, b));
                            break;
                        default:
                            System.out.println("Wrong operation type");
                            break;
                    }
                    break;
                    //outputting "Wrong calculator type" if no matching operation was found
                default:
                    System.out.println("Wrong calculator type");
                    break;
            }
        }
    }
    /**
     * this method scans input line and compares it with possible calculator types.
     * @return calculator type.
     */
    private CalculatorType readCalculator() {
        //scanning input line
        String typeOfOperation = scanner.next();
        //comparing input type with possible types and converting it in CalculatorType
        if (typeOfOperation.equals("INTEGER")) {
            return CalculatorType.INTEGER;
        } else if (typeOfOperation.equals("DOUBLE")) {
            return CalculatorType.DOUBLE;
        } else if (typeOfOperation.equals("STRING")) {
            return CalculatorType.STRING;
        } else {
            return CalculatorType.INCORRECT;
        }
    }
    /**
     * this method scans number of operations and checks if it satisfies given conditions.
     * @return integer number of operations or zero (if input number does not satisfy given conditions).
     */
    private int readCommandsNumber() {
        //creating variables for checking tasks condition
        int flag = 0;
        //scanning number of operations
        String numb = scanner.next();
        //using "try-catch" to check situations when scanned number is not an integer
        try {
            //converting string to integer
            int n = Integer.parseInt(numb);
        if (n >= 1 && n <= 50) {
            flag = 1;
        }
        if (flag == 0) {
            n = 0;
        }
        return n;
        } catch (Exception e) { //returning zero if conversion is impossible (input number is not integer)
            return 0;
        }
    }
    /**
     * this method checks if input calculator type is incorrect and outputs "Wrong calculator type".
     * @param err string containing calculator type.
     */
    private static void reportFatalError(String err) {
        //comparing argument string with "incorrect" type and throwing "Wrong calculator type" if they are equal
        if (err.equals("INCORRECT")) {
            System.out.println("Wrong calculator type");
            System.exit(0);
        }
    }
    /**
     * this method converts operation sign in operation type.
     * @param operation string containing sign of operation.
     * @return operation type.
     */
    private OperationType parseOperation(String operation) {
        //comparing argument string with operations signs to determine its type
        if (operation.equals("+")) {
            return OperationType.ADDITION;
        } else if (operation.equals("-")) {
            return OperationType.SUBTRACTION;
        } else if (operation.equals("*")) {
            return OperationType.MULTIPLICATION;
        } else if (operation.equals("/")) {
            return OperationType.DIVISION;
        } else {
            return OperationType.INCORRECT;
        }
    }
}
/**
 * enumeration containing possible calculator types.
 */
 enum CalculatorType {
    /**
     * integer calculator type.
     */
    INTEGER,
    /**
     * double calculator type.
     */
    DOUBLE,
    /**
     * string calculator type.
     */
    STRING,
    /**
     * incorrect calculator type.
     */
    INCORRECT
}
/**
 * enumeration containing possible operation types.
 */
enum OperationType {
    /**
     * addition operation type.
     */
    ADDITION,
    /**
     * subtraction operation type.
     */
    SUBTRACTION,
    /**
     * multiplication operation type.
     */
    MULTIPLICATION,
    /**
     * division operation type.
     */
    DIVISION,
    /**
     * incorrect operation type.
     */
    INCORRECT
}
/**
 * abstract class for calculators for different operands types.
 */
abstract class Calculator {
    /**
     * method for implementing addition.
     * @param a first term.
     * @param b second term.
     * @return sum.
     */
    abstract String add(String a, String b);
    /**
     * method for implementing subtraction.
     * @param a minuend.
     * @param b subtrahend.
     * @return result of subtraction.
     */
    abstract String subtract(String a, String b);
    /**
     * method for implementing multiplication.
     * @param a first factor.
     * @param b second factor.
     * @return product.
     */
    abstract String multiply(String a, String b);
    /**
     * method for implementing division.
     * @param a dividend.
     * @param b divisor.
     * @return quotient.
     */
    abstract String divide(String a, String b);
}
/**
 * calculator for performing integer operations.
 */
class IntegerCalculator extends Calculator {
    //performing integer addition
    //if operands are not integers outputting "Wrong argument type"
    @Override
    String add(String a, String b) {
        try {
            int i = Integer.parseInt(a);
            int j = Integer.parseInt(b);
            return Integer.toString(i + j);
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //performing integer subtraction
    //if operands are not integers outputting "Wrong argument type"
    @Override
    String subtract(String a, String b) {
        try {
            int i = Integer.parseInt(a);
            int j = Integer.parseInt(b);
            return Integer.toString(i - j);
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //performing integer multiplication
    //if operands are not integers outputting "Wrong argument type"
    @Override
    String multiply(String a, String b) {
        try {
            int i = Integer.parseInt(a);
            int j = Integer.parseInt(b);
            return Integer.toString(i * j);
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //performing integer division
    //if operands are not integers outputting "Wrong argument type"
    @Override
    String divide(String a, String b) {
        try {
            int i = Integer.parseInt(a);
            int j = Integer.parseInt(b);
            //in case of division by zero outputting "Division by zero"
            if (j == 0) {
                return "Division by zero";
            } else {
                return Integer.toString(i / j);
            }
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
}
/**
 * calculator for performing double operations.
 */
class DoubleCalculator extends Calculator {
    //performing double addition
    //if operands are not doubles outputting "Wrong argument type"
    @Override
    String add(String a, String b) {
        try {
            double i = Double.parseDouble(a);
            double j = Double.parseDouble(b);
            return Double.toString(i + j);
        }  catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //performing double subtraction
    //if operands are not doubles outputting "Wrong argument type"
    @Override
    String subtract(String a, String b) {
        try {
            double i = Double.parseDouble(a);
            double j = Double.parseDouble(b);
            return Double.toString(i - j);
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //performing double multiplication
    //if operands are not doubles outputting "Wrong argument type"
    @Override
    String multiply(String a, String b) {
        try {
            double i = Double.parseDouble(a);
            double j = Double.parseDouble(b);
            return Double.toString(i * j);
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //performing double division
    //if operands are not doubles outputting "Wrong argument type"
    @Override
    public String divide(String a, String b) {
            try {
                double i = Double.parseDouble(a);
                double j = Double.parseDouble(b);
                //in case of division by zero outputting "Division by zero"
                if (j == 0) {
                    return "Division by zero";
                } else {
                    return Double.toString(i / j);
                }
            } catch (Exception e) {
                return "Wrong argument type";
            }
    }
}
/**
 * calculator for string operations.
 */
class StringCalculator extends Calculator {
    //performing string addition
    @Override
    String add(String a, String b) {
        return a + b;
    }
    //outputting "Unsupported operation for strings" in case of string subtraction
    @Override
    public String subtract(String a, String b) {
        return "Unsupported operation for strings";
    }
    //repeating string given by first operand n times, where n is integer number given be the second operand
    //outputting "Wrong argument type" if the second operand is not positive integer number
    @Override
    public String multiply(String a, String b) {
        try {
            int i = Integer.parseInt(b);
            if (i > 0) {
                String answer = "";
                for (int j = 0; j < i; j++) {
                    answer += a;
                }
                return answer;
            } else {
                return "Wrong argument type";
            }
        } catch (Exception e) {
            return "Wrong argument type";
        }
    }
    //outputting "Unsupported operation for strings" in case of string division
    @Override
    String divide(String a, String b) {
        return "Unsupported operation for strings";
    }
}
