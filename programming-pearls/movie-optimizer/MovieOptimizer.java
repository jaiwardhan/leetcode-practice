import java.util.*;
import java.lang.*;
import java.io.*;

public class MovieOptimizer {
    ArrayList<MovieSchedule> movies = new ArrayList<MovieSchedule>();

    public void ingestMovie(int start, int end, String s) {
        this.movies.add(new MovieSchedule(start, end, s));
    }

    public void findBest() {
        // Sort by end time
        this.movies.sort(new Comparator<MovieSchedule>() {
            public int compare(MovieSchedule a, MovieSchedule b) {
                return a.endTime - b.endTime;
            }
        });
        ArrayList<MovieSchedule> selections = new ArrayList<MovieSchedule>();
        selections.add(this.movies.get(0));
        this.movies.forEach((eachMovie) -> {
            int latestEndTime = selections.get(selections.size()-1).endTime;
            if(latestEndTime < eachMovie.startTime) {
                selections.add(eachMovie);
            }
        });

        // We should now have what we want
        selections.forEach((i) -> { 
            System.out.println(String.format("%s, %d:%d", i.name, i.startTime, i.endTime));
        });
    }

}
