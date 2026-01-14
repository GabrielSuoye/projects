import java.util.concurrent.*;
import java.util.concurrent.locks.*;
import java.util.LinkedList;

public class ConsumerProducer {

    private static Buffer buffer = new Buffer();

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.execute(new ProducerTask());
        executor.execute(new ConsumerTask());
        executor.shutdown();
    }

    // Producer task
    private static class ProducerTask implements Runnable {
        public void run() {
            try {
                int i = 1;
                while (true) {
                    System.out.println("Producer writes " + i);
                    buffer.write(i++);
                    Thread.sleep((int) (Math.random() * 10000));
                }
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
    }

    // Consumer task
    private static class ConsumerTask implements Runnable {
        public void run() {
            try {
                while (true) {
                    System.out.println("\t\t\tConsumer reads " + buffer.read());
                    Thread.sleep((int) (Math.random() * 10000));
                }
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
    }

    // Buffer class
    private static class Buffer {
        private static final int CAPACITY = 3; // buffer size changed to 3
        private LinkedList<Integer> queue = new LinkedList<>();

        // Create a lock
        private static Lock lock = new ReentrantLock();

        // Create conditions
        private static Condition notEmpty = lock.newCondition();
        private static Condition notFull = lock.newCondition();

        public void write(int value) throws InterruptedException {
            lock.lock();
            try {
                while (queue.size() == CAPACITY) {
                    System.out.println("Wait for notFull condition");
                    notFull.await();
                }
                queue.offer(value);
                notEmpty.signal();
            } finally {
                lock.unlock();
            }
        }

        public int read() throws InterruptedException {
            lock.lock();
            try {
                while (queue.isEmpty()) {
                    System.out.println("\t\t\tWait for notEmpty condition");
                    notEmpty.await();
                }
                int value = queue.remove();
                notFull.signal();
                return value;
            } finally {
                lock.unlock();
            }
        }
    }
}