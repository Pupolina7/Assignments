import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
//D:\IdeaProjects\Assignment 5\src\input.txt
public final class Main {
    private Main() { };
    public static void main(String[] args) {
            try {
                File input = new File("D:\\IdeaProjects\\Assignment 5\\src\\input.txt");
                Scanner scanner = new Scanner(input);
                int d = Integer.parseInt(scanner.nextLine());
                float g = Float.parseFloat(scanner.nextLine());
                int n = Integer.parseInt(scanner.nextLine());
                List<Animal> animals = new ArrayList<>();
                final int maxGrass = 100;
                if (g < 0 || g > maxGrass) {
                    System.out.println(new GrassOutOfBoundsException().getMessage());
                    System.exit(0);
                }
                Field field = new Field(g);
                final int maxDays = 30;
                final int maxAnimals = 20;
                if (d < 1 || d > maxDays || n < 1 || n > maxAnimals) {
                    System.out.println(new InvalidInputsException().getMessage());
                    System.exit(0);
                }
                for (int i = 0; i < n; i++) {
                    String inputs = scanner.nextLine();
                    String[] subStr = inputs.split(" ");
                    final int four = 4;
                    if (subStr.length != four) {
                        System.out.println(new InvalidNumberOfAnimalParametersException().getMessage());
                        System.exit(0);
                    }
                    String animal = subStr[0];
                    float weight;
                    float energy;
                    float speed;
                    final int two = 2;
                    final int three = 3;
                    weight = Float.parseFloat(subStr[1]);
                    energy = Float.parseFloat(subStr[three]);
                    speed = Float.parseFloat(subStr[two]);
                    final int minWeight = 5;
                    final int maxWeight = 200;
                    if (weight < minWeight || weight > maxWeight) {
                        System.out.println(new WeightOutOfBoundsException().getMessage());
                        System.exit(0);
                    }
                    final int minSpeed = 5;
                    final int maxSpeed = 60;
                    if (speed < minSpeed || speed > maxSpeed) {
                        System.out.println(new SpeedOutOfBoundsException().getMessage());
                        System.exit(0);
                    }
                    if (energy < 0 || energy > maxGrass) {
                        System.out.println(new EnergyOutOfBoundsException().getMessage());
                        System.exit(0);
                    }
                    switch (animal) {
                        case "Zebra":
                            animals.add(new Zebra(weight, speed, energy));
                            break;
                        case "Boar":
                            animals.add(new Boar(weight, speed, energy));
                            break;
                        case "Lion":
                            animals.add(new Lion(weight, speed, energy));
                            break;
                        default:
                            System.out.println(new InvalidInputsException().getMessage());
                            System.exit(0);
                    }
                }
                    int j = 0;
                    while (j < animals.size()) {
                        if (animals.get(j).getEnergy() <= 0) {
                            animals.remove(j);
                            j--;
                        }
                        j++;
                    }
                    for (int i = 0; i < d; i++) {
                        j = 0;
                        while (j < animals.size()) {
                            String animal = animals.get(j).getClass().getName();
                            switch (animal) {
                                case "Zebra":
                                    ((Zebra) animals.get(j)).grazelnTheField((Zebra) animals.get(j), field);
                                    break;
                                case "Lion":
                                    String output = ((Lion) animals.get(j)).choosePrey(animals, (Lion) animals.get(j),
                                            j);
                                    if (!output.equals("check")) {
                                        System.out.println(output);
                                    }
                                    break;
                                case "Boar":
                                    ((Boar) animals.get(j)).grazelnTheField((Boar) animals.get(j), field);
                                    String out = ((Boar) animals.get(j)).choosePrey(animals, (Boar) animals.get(j), j);
                                    if (!out.equals("check")) {
                                        System.out.println(out);
                                    }
                                    break;
                                default:
                                    System.out.println(new InvalidInputsException().getMessage());
                                    System.exit(0);
                            }
                            j++;
                        }
                        field.grassGrow();
                        j = 0;
                        while (j < animals.size()) {
                            animals.get(j).decrementEnergy(-1);
                            if (animals.get(j).getEnergy() <= 0) {
                                animals.remove(j);
                                j--;
                            }
                            j++;
                        }
                    }
                j = 0;
                   while (j < animals.size()) {
                        animals.get(j).makeSound();
                        j++;
                    }
            } catch (Exception e) {
                System.out.println(new InvalidInputsException().getMessage());
            }
        }
    }

abstract class Animal {
    private final float weight;
    private final float speed;
    private float energy;
    protected Animal(float weighT, float speeD, float energY) {
        this.weight = weighT;
        this.speed = speeD;
        this.energy = energY;
    }

    public float getWeight() {
        return weight;
    }
    public float getSpeed() {
        return speed;
    }
    public float getEnergy() {
        return energy;
    }
    public void decrementEnergy(float addEnergy) {
        this.energy += addEnergy;
        final int maxEnergy = 100;
        if (this.energy > maxEnergy) {
            this.energy = maxEnergy;
        }
    }
    abstract void makeSound();

}
class Lion extends Animal implements Carnivore {
    protected Lion(float weight, float speed, float energy) {
        super(weight, speed, energy);
    }
    public void makeSound() {
        System.out.println("Roar");
    }

    @Override
    public String choosePrey(List<Animal> animals, Animal t, int i) {
        return Carnivore.super.choosePrey(animals, t, i);
    }
}
class Zebra extends Animal implements Herbevore {
    protected Zebra(float weight, float speed, float energy) {
        super(weight, speed, energy);
    }
    @Override
    void makeSound() {
        System.out.println("Ihoho");
    }

    @Override
    public void grazelnTheField(Animal animal, Field field) {
        Herbevore.super.grazelnTheField(animal, field);
    }
}
class Boar extends Animal implements Omnivores {
    protected Boar(float weight, float speed, float energy) {
        super(weight, speed, energy);
    }
    @Override
    void makeSound() {
        System.out.println("Oink");
    }

    @Override
    public void grazelnTheField(Animal animal, Field field) {
        Omnivores.super.grazelnTheField(animal, field);
    }

    @Override
    public String choosePrey(List<Animal> animals, Animal t, int i) {
        return Omnivores.super.choosePrey(animals, t, i);
    }
}

class WeightOutOfBoundsException extends Exception {
    public String getMessage() {
        return "The weight is out of bounds";
    }
}
class EnergyOutOfBoundsException extends Exception {
    public String getMessage() {
        return "The energy is out of bounds";
    }
}
class SpeedOutOfBoundsException extends Exception {
    public String getMessage() {
        return "The speed is out of bounds";
    }
}
class GrassOutOfBoundsException extends Exception {
    public String getMessage() {
        return "The grass is out of bounds";
    }
}
class InvalidInputsException extends Exception {
    public String getMessage() {
        return "Invalid inputs";
    }
}
class InvalidNumberOfAnimalParametersException extends Exception {
    public String getMessage() {
        return "Invalid number of animal parameters";
    }
}
class Field {
    private float grassAmount;
    Field(float grasSAmount) {
        this.grassAmount = grasSAmount;
    }
    public float getGrassAmount() {
        return grassAmount;
    }
    protected final int maxGrass = 100;
    public void grassGrow() {
        grassAmount = 2 * grassAmount;
        if (grassAmount > maxGrass) {
            grassAmount = maxGrass;
        }
    }
    public void editField(float grass) {
        this.grassAmount -= grass;
    }
}
interface Carnivore {
    default String choosePrey(List<Animal> animals, Animal t, int i) {
        String message = "check";
        String animal = t.getClass().getName();
        String prey;
        if (animals.size() == 1) {
            message = "Self-hunting is not allowed";
        } else if (i == (animals.size() - 1)) {
            prey = animals.get(0).getClass().getName();
            if (!(prey.equals(animal))) {
                if ((animals.get(i).getEnergy() > animals.get(0).getEnergy())
                        || (animals.get(i).getSpeed() > animals.get(0).getSpeed())) {
                    animals.get(i).decrementEnergy(animals.get(0).getWeight());
                    animals.get(0).decrementEnergy(-1 * (animals.get(0).getEnergy()));
                    animals.remove(0);
                } else {
                    message = "The prey is too strong or too fast to attack";
                }
            } else {
                message = "Cannibalism is not allowed";
            }
        } else {
            if (!((animals.get(i + 1).getClass().getName()).equals(animal))) {
            if ((animals.get(i).getEnergy() > animals.get(i + 1).getEnergy())
                    || (animals.get(i).getSpeed() > animals.get(i + 1).getSpeed())) {
                animals.get(i).decrementEnergy(animals.get(i + 1).getWeight());
                animals.get(i + 1).decrementEnergy(-1 * (animals.get(i + 1).getEnergy()));
                animals.remove(i + 1);
            } else {
                message = "The prey is too strong or too fast to attack";
            }
        } else {
            message = "Cannibalism is not allowed";
        }
    }
        return message;
    }
}
interface Herbevore {
    int TEN = 10;
    default void grazelnTheField(Animal animal, Field field) {
        if ((animal.getWeight() / TEN) < field.getGrassAmount()) {
            animal.decrementEnergy(animal.getWeight() / TEN);
            field.editField(animal.getWeight() / TEN);
        }
    }
}
interface Omnivores extends Herbevore, Carnivore {
}
