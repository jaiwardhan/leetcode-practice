public class Test {

	public static void main(String[] args) {
		// Test 1
		// (
		MovieOptimizer mo = new MovieOptimizer();
		mo.ingestMovie(0, 10, "The President's Algorist");
        mo.ingestMovie(1, 8, "Discrete Math");
        mo.ingestMovie(3, 16, "Tarzan");
        mo.ingestMovie(9, 17, "Halting State");
        mo.ingestMovie(14, 20, "Steiner's Tree");
        mo.ingestMovie(18, 30, "The Four Volume Problem");
        mo.ingestMovie(20, 29, "Prog Challenges");
        mo.ingestMovie(27, 60, "Process Terminated");
        mo.ingestMovie(35, 61, "Calculated Bets");

        mo.findBest();
}
}
