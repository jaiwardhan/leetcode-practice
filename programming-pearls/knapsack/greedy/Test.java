import java.lang.*;
import java.util.*;

public class Test {
    public static void main(String[] args) {
        GreedyKnapsack gk = new GreedyKnapsack();
        ArrayList<Integer> set = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));
        Integer target = 13;
        gk.findTarget(set, target);
        System.out.println("---");
        gk.findTargetAll(set, 10);
    }
}