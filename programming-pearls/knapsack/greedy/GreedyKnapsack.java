import java.lang.*;
import java.util.*;

public class GreedyKnapsack {

    ArrayList<Integer> set = new ArrayList<Integer>();
    ArrayList<Integer> validIdx = new ArrayList<Integer>();
    Integer target = 0;
    
    public void findTarget(ArrayList<Integer> set, Integer target) {
        this.set = set;
        this.target = 0;

        this.findHelper(0, target);
        if(this.validIdx.size() < 0) {
            System.out.println("No valid set found");
        } else {
            Integer i = this.validIdx.size()-1;
            while(i >= 0) {
                Integer idx = this.validIdx.get(i);
                System.out.println(this.set.get(idx));
                i -= 1;
            }
        }
    }

    public void findTargetAll(ArrayList<Integer> set, Integer target) {
        this.set = set;
        this.target = target;
        ArrayList<ArrayList<Integer>> findings = this.findHelperAll(0, target);
        if(findings.size() == 0) {
            System.out.println("No valid target sets found");
            return;
        }

        findings.forEach(i -> {
            Integer index = i.size()-1;
            while(index >= 0) {
                Integer validIndex = i.get(index);
                System.out.println(this.set.get(validIndex));
                index -= 1;
            }
            System.out.println("----");
        });

    }

    public boolean findHelper(Integer index, Integer rSum) {
        if(rSum == 0) {
            return true;
        }

        if(index >= this.set.size() || rSum < 0) {
            return false;
        }

        boolean found = false;
        while(!found && index < this.set.size()) {
            found = this.findHelper(index+1, rSum - this.set.get(index));
            index += 1;
        }

        if(found) {
            this.validIdx.add(index-1);
            return true;
        }

        return false;
    }

    public ArrayList<ArrayList<Integer>> findHelperAll(Integer index, Integer rSum) {
        if(rSum < 0 || index >= this.set.size()) {
            return null;
        }
        ArrayList<ArrayList<Integer>> validIdxAt = new ArrayList<ArrayList<Integer>>();
        if(rSum == 0) {
            return validIdxAt;
        }

        while(index < this.set.size()) {
            ArrayList<ArrayList<Integer>> findings = this.findHelperAll(index+1, rSum - this.set.get(index));
            if(findings != null) {
                // We found something
                findings.forEach(f -> {
                    ArrayList<Integer> g = f;
                    g.add(index);
                    validIdxAt.add(g);
                });
            }

            index += 1;
        }
        return validIdxAt;
    }

}
