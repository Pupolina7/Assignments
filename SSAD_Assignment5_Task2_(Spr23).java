//Polina Pushkareva
//Assignment 5 Task 3
//Observer design pattern
import java.util.ArrayList;
import java.util.List;
class Runner {
    public static void main(String[] args) {
        User user1 = new User("Alice");
        User user2 = new User("Bob");
        Channel channel1 = new Channel("Discovery");
        Channel channel2 = new Channel("Pewdiepie");
        Channel channel3 = new Channel("Innopolis");
        channel1.subscribe(user1);
        channel2.subscribe(user2);
        channel3.subscribe(user1);
        channel3.subscribe(user2);
        channel1.publish(new Video("Animals in Australia"));
        channel2.publish(new Shorts("Minicraft"));
        channel3.publish(new LiveStream("Report from rainforest"));
        channel3.unsubscribe(user1);
        channel1.publish(new Video("Scuba diving in Great Barrier Reef"));
        channel2.publish(new Shorts("Fortnite montage"));
        channel3.publish(new LiveStream("Jungle survival tips"));
    }
}
class Channel {
    List<User> subscribers = new ArrayList<>();
    List<Content> contents = new ArrayList<>();
    private String name;
    Channel (String name) {
        this.name=name;
    }
    public String getName() {
        return name;
    }
    void publish (Content content) {
        contents.add(content);
        for(User subscriber : subscribers) {
            System.out.println(subscriber.getName()+": Channel "+name+content.notifySubscribers());
        }
    }
    void subscribe (User user) {
        subscribers.add(user);
    }
    void unsubscribe (User user) {
        subscribers.remove(user);
    }
}
class User{
    private String name;
    User (String name) {
        this.name=name;
    }
    public String getName() {
        return name;
    }
}
interface Content{
    String notifySubscribers();
}
class Video implements Content{
    String name;
    Video(String name) {
        this.name=name;
    }
    @Override
    public String notifySubscribers() {
        return " published new Video: "+name;
    }
}
class Shorts implements Content {
    String name;
    Shorts(String name) {
        this.name=name;
    }
    @Override
    public String notifySubscribers() {
        return " published new Shorts: "+name;
    }
}
class LiveStream implements Content {
    String name;
    LiveStream (String name) {
        this.name=name;
    }
    @Override
    public String notifySubscribers() {
        return " is going life: "+name;
    }
}
