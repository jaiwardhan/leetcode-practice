import java.util.*;

public class GrayCodeSubset {

	public static ArrayList<StringBuilder> getAtLevel(int level) {
		if (level <= 0) {
			ArrayList<StringBuilder> def = new ArrayList<StringBuilder>();
			def.add(new StringBuilder(""));
			return def;
		}
		ArrayList<StringBuilder> set = GrayCodeSubset.getAtLevel(level - 1);
		ArrayList<StringBuilder> reverseSet = new ArrayList<StringBuilder>();
		for (int i = set.size() - 1; i >= 0; i--) {
			reverseSet.add(set.get(i));
		}
		int setSize = set.size();

		for (int i = 0; i < setSize; i++) {
			set.set(i, (new StringBuilder("0")).append(set.get(i)));
			reverseSet.set(i, (new StringBuilder("1")).append(reverseSet.get(i)));
		}
		reverseSet.forEach((eachSet) -> {
			set.add(eachSet);
		});
		return set;
	}

	public static void get(String fromSet) {
		StringBuilder fromSetSb = new StringBuilder(fromSet);
		ArrayList<StringBuilder> grayCodes = GrayCodeSubset.getAtLevel(fromSetSb.length());

		ArrayList<StringBuilder> subsets = new ArrayList<StringBuilder>();
		grayCodes.forEach((eachCode) -> {
			StringBuilder sb = new StringBuilder("{");
			for (int i = 0; i < eachCode.length(); i++) {
				if (eachCode.charAt(i) == '1')
					sb.append(fromSetSb.charAt(i));
			}
			sb.append("}");
			subsets.add(sb);
		});

		subsets.forEach(i -> System.out.println(i));
		System.out.println("---------");
	}
}
