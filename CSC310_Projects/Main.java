import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ThreadLocalRandom;
import java.util.Random;

class FleetTracker {
    private final Map<String, Location> vehicleLocations = new ConcurrentHashMap<>();

    public void updateLocation(String vehicleId, double lat, double lon) {
        vehicleLocations.put(vehicleId, new Location(lat, lon));
        System.out.println("[Update] " + vehicleId + " moved to " + lat + ", " + lon);
    }

    public Map<String, Location> getFleetStatus() {
        return Map.copyOf(vehicleLocations);
    }

    public record Location(double lat, double lon) {}
}

class Vehicle implements Runnable {
    private final String vehicleId;
    private final FleetTracker tracker; 

    private final Random random = new Random();

    public Vehicle(String vehicleId, FleetTracker tracker) {
        this.vehicleId = vehicleId;
        this.tracker = tracker;
    }
    @Override
    public void run() {
        try {
            while  (!Thread.currentThread().isInterrupted()) {
                // Simulate moving
                double lat = 40.0 + ThreadLocalRandom.current().nextDouble();
                double lon = -74.0 + ThreadLocalRandom.current().nextDouble();
                tracker.updateLocation(vehicleId, lat, lon);

                // Sleep to simulate interval between GPS pings
                Thread.sleep(2000 + random.nextInt(3000));
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println(vehicleId + " tracking stopped.");
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        FleetTracker tracker = new FleetTracker();
        
        ExecutorService pool = Executors.newFixedThreadPool(10);
        pool.submit(new Vehicle("Vehicle1", tracker)); 
        pool.submit(new Vehicle("Vehicle2", tracker));
        pool.submit(new Vehicle("Vehicle3", tracker));
        pool.submit(new Vehicle("Vehicle4", tracker));
        pool.submit(new Vehicle("Vehicle5", tracker));
        pool.submit(new Vehicle("Vehicle6", tracker));
        pool.submit(new Vehicle("Vehicle7", tracker));
        pool.submit(new Vehicle("Vehicle8", tracker));
        pool.submit(new Vehicle("Vehicle9", tracker));
        pool.submit(new Vehicle("Vehicle10", tracker));

        Thread.sleep(15000);

        pool.shutdownNow();

    }
}

