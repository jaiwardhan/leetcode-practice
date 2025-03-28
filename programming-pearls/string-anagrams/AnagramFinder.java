import java.util.*;
import java.lang.*;
import java.io.*;


public class AnagramFinder {
                HashMap<String, HashSet<String> > lookup = new HashMap<String, HashSet<String> >();
                AnagramFinder() { }

                public void ingest(String s) {
                        char[] chars = s.toCharArray();
                        Arrays.sort(chars);
                        String sorted = new String(chars);
                        if(!lookup.containsKey(sorted)) {
                                lookup.put(sorted, new HashSet<String>());
                        }
                        lookup.get(sorted).add(s);
                }

                public void listAnagrams() {
                        this.lookup.forEach((key, value) -> {
                                value.forEach((v) -> System.out.println(v));
                                System.out.println();
                        });
                }
        }
