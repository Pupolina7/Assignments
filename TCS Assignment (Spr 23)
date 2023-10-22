//Polina Pushkareva CS_01

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static Main main = new Main();
    public static void main(String[] args) {
        try {
            //"opening" input file
            File input = new File("input.txt");
            //declaring scanner from input
            Scanner scanner = new Scanner(input);
            //scanning the line, containing states
            String scan = scanner.nextLine();
            //check if the input is malformed
            if (!scan.contains("states=[") || !scan.contains("]")) {
                System.out.println("E1: Input file is malformed");
                System.exit(0);
            }
            //making a substring of elements between []
            scan = scan.substring(scan.indexOf("[") + 1, scan.indexOf("]"));
            //splitting states (getting array of states)
            String[] states = scan.split(",");
            //scanning the line, containing alphabet symbols
            scan = scanner.nextLine();
            //check if the input is malformed
            if (!scan.contains("alpha=[") || !scan.contains("]")) {
                System.out.println("E1: Input file is malformed");
                System.exit(0);
            }
            //making a substring of elements between []
            scan = scan.substring(scan.indexOf("[") + 1, scan.indexOf("]"));
            //splitting alphabet (getting array of alphabet symbols)
            String[] alpha = scan.split(",");
            //scanning the line, containing initial state(s)
            scan = scanner.nextLine();
            //check if the input is malformed
            if (!scan.contains("initial=[") || !scan.contains("]")) {
                System.out.println("E1: Input file is malformed");
                System.exit(0);
            }
            //making a substring of elements between []
            scan = scan.substring(scan.indexOf("[") + 1, scan.indexOf("]"));
            //splitting initial states (getting array of initial states)
            String[] initSt = scan.split(",");
            //scanning the line, containing final state(s)
            scan = scanner.nextLine();
            //check if the input is malformed
            if (!scan.contains("accepting=[") || !scan.contains("]")) {
                System.out.println("E1: Input file is malformed");
                System.exit(0);
            }
            //making a substring of elements between []
            scan = scan.substring(scan.indexOf("[") + 1, scan.indexOf("]"));
            //splitting final states (getting array of accepting states)
            String[] finalSt = scan.split(",");
            //scanning the line, containing transitions
            scan = scanner.nextLine();
            //check if the input is malformed
            if (!scan.contains("trans=[") || !scan.contains("]")) {
                System.out.println("E1: Input file is malformed");
                System.exit(0);
            }
            //making a substring of elements between []
            scan = scan.substring(scan.indexOf("[") + 1, scan.indexOf("]"));
            //declaring a string to use it in error outputs
            String remember = null;
            //splitting transitions (getting array of states in transitions and transitions)
            //1st, 4th, 7th and so on elements contain a transition, other contain states
            String[] trans = scan.split("[>,]");
            //declaring boolean variable to use it while working with errors
            boolean flag = true;
            //checking if states contain not only latin letters and numbers
            for (String s : states) {
                if (!s.matches("[a-zA-Z0-9]+")) {
                    System.out.println("E1: Input file is malformed");
                    System.exit(0);
                }
            }
            //checking if alphabet symbols contain not only latin letters, numbers, and "_" sign
            for (String a : alpha) {
                if (!a.matches("[a-zA-Z0-9_]+")) {
                    System.out.println("E1: Input file is malformed");
                    System.exit(0);
                }
            }
            if (initSt.length > 1) {
                System.out.println("E1: Input file is malformed");
                System.exit(0);
            }
            //checking if the input contains initial state
            if (initSt.length == 0 || (initSt.length == 1 && initSt[0].length() == 0)) {
                System.out.println("E2: Initial state is not defined");
                System.exit(0);
            } else if (initSt.length == 1) {
                //checking if all states are in the set of sates
                for (String s : states) {
                    if (initSt[0].equals(s)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    System.out.println("E4: A state '" + initSt[0] + "' is not in the set of states");
                    System.exit(0);
                }
            }
            //checking if accepting states are undefined
            if (finalSt.length == 0 || (finalSt.length == 1 && finalSt[0].length() == 0)) {
                System.out.println("E3: Set of accepting states is empty");
                System.exit(0);
            }
            //check if all accepting states are in the set of states
            for (int i = 0; i < finalSt.length; i++) {
                flag = false;
                if (finalSt[i].equals("")) {
                } else {
                    for (String state : states) {
                        if (finalSt[i].equals(state)) {
                            flag = false;
                            break;
                        } else {
                            flag = true;
                            remember = finalSt[i];
                        }
                    }
                }
                if (flag) {
                    System.out.println("E4: A state '" + remember + "' is not in the set of states");
                    System.exit(0);
                }
            }
            //performing checks for transitions
            for (int i = 0; i < trans.length; i = i + 3) {
                flag = false;
                //if the first state in the transition doesn't belong to the set of states outputting Error 4
                for (String state : states) {
                    if (!trans[i].equals(state)) {
                        flag = true;
                        remember = trans[i];
                    } else {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    System.out.println("E4: A state '" + remember + "' is not in the set of states");
                    System.exit(0);
                }
                //if the transition doesn't belong to the alphabet outputting Error 5
                flag = false;
                for (String alph : alpha) {
                    if (!trans[i + 1].equals(alph)) {
                        flag = true;
                        remember = trans[i + 1];
                    } else {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    System.out.println("E5: A transition '" + remember + "' is not represented in the alphabet\n");
                    System.exit(0);
                }
                //if the second state in the transition doesn't belong to the set of states outputting Error 4
                flag = false;
                for (String state : states) {
                    if (!trans[i + 2].equals(state)) {
                        flag = true;
                        remember = trans[i + 2];
                    } else {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    System.out.println("E4: A state '" + remember + "' is not in the set of states");
                    System.exit(0);
                }
            }
            //creating a hashmap to count the number of transitions for each state
            HashMap<String, HashMap<String, Integer>> numberOfTrans = new HashMap<>();
            //creating a hashmap that will contain all possible destinations from every state (in both directions)
            HashMap<String, ArrayList<String>> bothSidesTransitions = new HashMap<>();
            //creating a hashmap to use to check if the transition is visited from some state (in both directions)
            //will be used for checking on disjoint states (E6)
            HashMap<String, Boolean> bothSidesTransitionsVisited = new HashMap<>();
            for (int i = 0; i < trans.length; i = i + 3) {
                //for each first in transition adding false to the corresponding key in the hashmap (will be needed later)
                //adding values for both directions
                bothSidesTransitionsVisited.putIfAbsent(trans[i], false);
                bothSidesTransitionsVisited.putIfAbsent(trans[i + 2], false);
                //adding current transition in the corresponding hashmap (both directions)
                if (bothSidesTransitions.get(trans[i]) == null) {
                    bothSidesTransitions.put(trans[i], new ArrayList<>());
                    bothSidesTransitions.get(trans[i]).add(trans[i + 2]);
                } else {
                    bothSidesTransitions.get(trans[i]).add(trans[i + 2]);
                }
                if (bothSidesTransitions.get(trans[i + 2]) == null) {
                    bothSidesTransitions.put(trans[i + 2], new ArrayList<>());
                    bothSidesTransitions.get(trans[i + 2]).add(trans[i]);
                } else {
                    bothSidesTransitions.get(trans[i + 2]).add(trans[i]);
                }
                //counting the total number of transitions FROM each state using corresponding hashmap
                numberOfTrans.computeIfAbsent(trans[i], k -> new HashMap<>());
                if (numberOfTrans.get(trans[i]).get(trans[i + 1]) == null) {
                    numberOfTrans.get(trans[i]).put(trans[i + 1], 1);
                } else {
                    numberOfTrans.get(trans[i]).put(trans[i + 1], numberOfTrans.get(trans[i]).get(trans[i + 1]) + 1);
                }
            }
            //Using depth-first search function for transitions in one and both directions (declared later)
            main.DFS(initSt[0], bothSidesTransitions, bothSidesTransitionsVisited);
            //if some transitions in both sides are not visited outputting E6
            for (String state : states) {
                if (bothSidesTransitionsVisited.containsKey(state)) {
                    if (!bothSidesTransitionsVisited.get(state)) {
                        System.out.println("E6: Some states are disjoint");
                        System.exit(0);
                    }
                } else {
                    System.out.println("E6: Some states are disjoint");
                    System.exit(0);
                }
            }
            //if the FSA has some states where one transitions transfers to different states then the FSA is nondeterministic
            //outputting E7
            for (String state : states) {
                for (String a : alpha) {
                    if (numberOfTrans.containsKey(state)) {
                        if (numberOfTrans.get(state).get(a) == null) {
                        } else if (numberOfTrans.get(state).get(a) > 1) {
                            System.out.println("E7: FSA is nondeterministic");
                            System.exit(0);
                        }
                    }
                }
            }
            //declaring matrix for R^-1 with empty strings
            String[][] K_1 = new String[states.length][states.length];
            for (int i = 0; i < states.length; i++) {
                for (int j = 0; j < states.length; j++) {
                    K_1[i][j] = "";
                }
            }
            //declaring hash map contains pairs name-number
            Map<String, Integer> numberState = new HashMap<>();
            for (int i = 0; i < states.length; i++) {
                numberState.put(states[i], i);
            }
            //filling R^-1 matrix by the definition
            for (int i = 0; i < trans.length; i = i + 3) {
                K_1[numberState.get(trans[i])][numberState.get(trans[i + 2])] += ",";
                K_1[numberState.get(trans[i])][numberState.get(trans[i + 2])] += trans[i + 1];
            }
            //filling matrix by conditions in the task
            for (int i = 0; i < states.length; i++) {
                for (int j = 0; j < states.length; j++) {
                    if (K_1[i][j].length() == 0 && i!=j) {
                        //no transitions
                        K_1[i][j] = "{}";
                    } else {
                        String[] split = K_1[i][j].split(",");
                        //sorting transitions in lexographical order
                        Arrays.sort(split);
                        K_1[i][j] = "";
                        for (int k = 0; k < split.length; k++) {
                            if (split[k].length() != 0) {
                                K_1[i][j] += split[k];
                                if (k < (split.length - 1) && k != 0) {
                                    K_1[i][j] += "|";
                                }
                            }
                        }
                        //adding epsilon transition if needed
                        if (i == j) {
                            if (K_1[i][j].length() == 0) {
                                K_1[i][j] = "eps";
                            } else {
                                K_1[i][j] += "|eps";
                            }
                        }
                    }
                }
            }
            //declaring empty matrix R
            String[][] K = new String[states.length][states.length];
            for (int i = 0; i < states.length; i++) {
                for (int j = 0; j < states.length; j++) {
                    K[i][j] = "";
                }
            }
            int k = 0;
            //performing following steps one time lesser than the number of states
            while (k <= states.length - 1) {
                for (int i = 0; i < states.length; i++) {
                    for (int j = 0; j < states.length; j++) {
                        //adding regular expression by formula in the corresponding matrix cell
                            K[i][j] += "(" + K_1[i][k] + ")(" + K_1[k][k] + ")*(" + K_1[k][j] + ")|(" + K_1[i][j] + ")";
                    }
                }
                //moving elements from R matrix to R^-1 matrix
                //and erasing elements from R^-1 matrix
                for (int l = 0; l < states.length; l++) {
                    for (int p = 0; p < states.length; p++) {
                        K_1[l][p] = K[l][p];
                        K[l][p] = "";
                    }
                }
                k++;
            }
            //if FSA has only one final state outputting corresponding regular expression
            if (finalSt.length == 1) {
                System.out.println("("+K_1[numberState.get(initSt[0])][numberState.get(finalSt[0])]+")");
            } else{
                //otherwise, outputting regular expressions for all final states with | symbol between
            for (int i = 0; i < finalSt.length; i++) {
                System.out.print("(");
                System.out.print(K_1[numberState.get(initSt[0])][numberState.get(finalSt[i])]);
                if (i != finalSt.length - 1) {
                    System.out.print(")|");
                }
            }
                System.out.print(")");
        }
        } catch (Exception e) {
            System.out.println(new Exception().getMessage());
        }
    }
    //Depth-first search
    void DFS(String initState, HashMap<String, ArrayList<String>> transitions, HashMap<String, Boolean> visitedStates) {
        //filling the visited stages with "true" values
        visitedStates.put(initState, true);
        if (transitions.get(initState).isEmpty()) {
            return;
        }
        //going through all possible transitions
        for (String transition : transitions.get(initState)) {
            //if the transition is not visited returning on the previous transition
            if (!visitedStates.get(transition)) {
                //recorsive call
                DFS(transition, transitions, visitedStates);
            }
        }
    }
}
