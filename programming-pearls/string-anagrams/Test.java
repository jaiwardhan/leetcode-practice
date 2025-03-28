/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;


public class Test {

	public static void main(String[] args) {

		AnagramFinder af = new AnagramFinder();
                String[] examples = {"abc", "bac", "egg", "geg", "omg"};
                for(String s:examples) {
                        af.ingest(s);
                }
                af.listAnagrams();

	}
	
	public void runProgram() {
		AnagramFinder af = new AnagramFinder();
		String[] examples = {"abc", "bac", "egg", "geg", "omg"};
		for(String s:examples) {
			af.ingest(s);
		}
		af.listAnagrams();
	}
}



