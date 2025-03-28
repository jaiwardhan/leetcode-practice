import java.util.*;
import java.lang.*;

public class GreedyActor {
	ArrayList<MovieData> movieBook = new ArrayList<MovieData>();
	ArrayList<Integer> maxIncomeLookup = new ArrayList<Integer>();

	public void ingestMovie(MovieData movie) {
		this.movieBook.add(movie);
	}

	private int findBestSelection(int fromIndex) {
		int maxTillNow = 0;
		int i = fromIndex + 1;
		if (fromIndex >= this.movieBook.size())
			return 0;
		while (i < this.movieBook.size()) {
			if (this.movieBook.get(i).startTime > this.movieBook.get(fromIndex).endTime) {
				// Can accept this one
				if (this.maxIncomeLookup.get(i) == -1) {
					int bestTill = this.findBestSelection(i);
					maxTillNow = Math.max(maxTillNow, bestTill);
				} else {
					maxTillNow = Math.max(maxTillNow, this.maxIncomeLookup.get(i));
				}
			}
			i += 1;
		}
		int maxIncomeTill = maxTillNow + this.movieBook.get(fromIndex).payout;
		this.maxIncomeLookup.set(fromIndex, maxIncomeTill);
		return maxIncomeTill;
	}

	public void getSelection() {
		this.movieBook.sort(new Comparator<MovieData>() {
			public int compare(MovieData a, MovieData b) {
				return a.endTime - b.endTime;
			}
		});

		this.maxIncomeLookup = new ArrayList<Integer>();
		for (int i = 0; i < this.movieBook.size(); i++) {
			this.maxIncomeLookup.add(-1);
		}
		int totCovered = 0;
		int bestIncome = this.findBestSelection(0);
		System.out.println(String.format("The max you can earn is: %d", bestIncome));

	}

}
