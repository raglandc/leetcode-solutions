import java.util.*;

/**
 * @name:   Underground System
 * @author: Christopher M. Ragland II
 * @date:   July 21st, 2024
*/

class TravelData {
    String fromStation;
    Integer startTime;

    TravelData (String fs, Integer st) {
        this.fromStation = fs;
        this.startTime = st;
    }
}

class RouteData {
    Double total;
    Double count;

    RouteData() {
        this.total = 0.0;
        this.count = 0.0;
    }
}

class UndergroundSystem {
    HashMap<Integer, TravelData> travelerHashMap;
    HashMap<String, RouteData> stationHashMap;

    public UndergroundSystem () {
        this.travelerHashMap = new HashMap<>();
        this.stationHashMap = new HashMap<>();
    }

    public void checkIn (int id, String stationName, int t) {
        this.travelerHashMap.put(id, new TravelData(stationName, t));
    }

    public void checkOut (int id, String stationName, int t) {
        TravelData travelerData = travelerHashMap.get(id);
        String startStation = travelerData.fromStation;
        Integer startTime = travelerData.startTime;
        travelerHashMap.remove(id);
        String routeKey = getRouteKey(startStation, stationName);
        if (stationHashMap.get(routeKey) == null) {
            stationHashMap.put(routeKey, new RouteData());
        }
        stationHashMap.get(routeKey).total += (t - startTime);
        stationHashMap.get(routeKey).count += 1;
    }

    public double getAverageTime (String startStation, String endStation) {
        String routeKey = getRouteKey(startStation, endStation);
        RouteData routeData = stationHashMap.get(routeKey);
        Double total = routeData.total;
        Double count = routeData.count;
        Double result = total / count;
        System.out.println(result);
        return result;
    }

    private String getRouteKey(String fromStation, String toStation) {
        return fromStation + "->" + toStation;
    }

}

public class Main {
    public static void main(String[] args) {
        runTestOne();
        System.out.println("\n---- Starting Test Two ----\n");
        runTestTwo();
    }

    private static void runTestOne() {
        UndergroundSystem undergroundSystem = new UndergroundSystem();
        undergroundSystem.checkIn(45, "Leyton", 3);
        undergroundSystem.checkIn(32, "Paradise", 8);
        undergroundSystem.checkIn(27, "Leyton", 10);
        undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
        undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
        undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
        undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
        undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
        undergroundSystem.checkIn(10, "Leyton", 24);
        undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
        undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
        undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
    }

    private static void runTestTwo() {
        UndergroundSystem undergroundSystem = new UndergroundSystem();
        undergroundSystem.checkIn(10, "Leyton", 3);
        undergroundSystem.checkOut(10, "Paradise", 8); // Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
        undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000, (5) / 1 = 5
        undergroundSystem.checkIn(5, "Leyton", 10);
        undergroundSystem.checkOut(5, "Paradise", 16); // Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
        undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000, (5 + 6) / 2 = 5.5
        undergroundSystem.checkIn(2, "Leyton", 21);
        undergroundSystem.checkOut(2, "Paradise", 30); // Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
        undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667, (5 + 6 + 9) / 3 = 6.66667
    }
}
