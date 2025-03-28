public class Test {
	public static void main(String[] args) {
		GreedyActor greedyActor = new GreedyActor();
		greedyActor.ingestMovie(new MovieData(32, 45, 15));
		greedyActor.ingestMovie(new MovieData(15, 28, 10));
		greedyActor.ingestMovie(new MovieData(29, 35, 10));
		greedyActor.ingestMovie(new MovieData(32, 40, 2));
		greedyActor.ingestMovie(new MovieData(5, 30, 20));
		greedyActor.ingestMovie(new MovieData(2, 10, 10));

		greedyActor.getSelection();
	}
}

