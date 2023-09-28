public class Telemetry {
    public Log log() {
        return new Log();
    }
    public void update() {
        // Nothing for now.
    }
}

class Log {
    public void add(Object l) {
        System.out.println(l);
    }
}
