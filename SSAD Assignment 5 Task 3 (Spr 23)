//Polina Pushkareva
//Assignment 5 Task 3
//Flyweight and Visitor design patterns

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Flyweight flyweight = new Flyweight();
        List<Shape> shapes = new ArrayList<>();
        shapes.add(flyweight.getShape("triangle"));
        shapes.add(flyweight.getShape("triangle"));
        shapes.add(flyweight.getShape("circle"));
        shapes.add(flyweight.getShape("line"));
        shapes.add(flyweight.getShape("rectangle"));
        shapes.add(flyweight.getShape("circle"));
        shapes.add(flyweight.getShape("line"));
        for(Shape shape:shapes) {
            shape.export(shape);
            shape.draw(1,2);
        }
    }
}
/*
Flyweight design pattern allows to introduce only one copy of needed figures and use it whenever this concrete
figure is needed.
Here interface export represents "concept of visitor design pattern", it allows to perform special actions for
concrete figures types.
 */
class Color {
    //some needed implementation
}
class Flyweight {
    private final Map<String, Shape> shapes = new HashMap<>();
    public Shape getShape (String name) {
        Shape shape = shapes.get(name);
        if(shape==null) {
            switch (name) {
                case "rectangle":
                    System.out.println("Creating rectangle...");
                    shape = new Rectangle();
                    break;
                case "circle":
                    System.out.println("Creating circle...");
                    shape = new Circle();
                    break;
                case "triangle":
                    System.out.println("Creating triangle...");
                    shape = new Triangle();
                    break;
                case "line":
                    System.out.println("Creating line...");
                    shape = new Line();
                    break;
            }
            shapes.put(name, shape);
        } else {
            System.out.println("Using an already existing "+shape.getClass().getName()+"...");
        }
        return shape;
    }
}
interface Export {
    void export(Rectangle rectangle);
    void export(Circle circle);
    void export(Triangle triangle);
    void export(Line line);
}
abstract class Shape {
    Color fillColor;
    Color borderColor;
    double borderThickness;
    double coordinateX;
    double coordinateY;
    abstract void draw (double x, double y);
    void export(Shape shape) {
        if(shape instanceof Rectangle) {
            ((Rectangle)shape).export((Rectangle)shape);
        } else if(shape instanceof Circle) {
            ((Circle)shape).export((Circle) shape);
        } else if(shape instanceof Triangle) {
            ((Triangle)shape).export((Triangle) shape);
        } else if(shape instanceof Line) {
            ((Line)shape).export((Line) shape);
        }
    }
}
class Rectangle extends Shape implements Export{
    double length;
    double width;

    @Override
    void draw(double x, double y) {
        System.out.println("Drawing rectangle...");
    }

    @Override
    public void export(Rectangle rectangle) {
        System.out.println("Exporting rectangle...");
    }

    @Override
    public void export(Circle circle) {
        //do nothing
        System.out.println("circle");
    }

    @Override
    public void export(Triangle triangle) {
        //do nothing
        System.out.println("triangle");
    }

    @Override
    public void export(Line line) {
        //do nothing
        System.out.println("line");
    }
}
class Circle extends Shape implements Export{
    double radius;

    @Override
    void draw(double x, double y) {
        System.out.println("Drawing circle...");
    }

    @Override
    public void export(Rectangle rectangle) {
        //do nothing
        System.out.println("rectangle");
    }

    @Override
    public void export(Circle circle) {
        System.out.println("Exporting circle...");
    }

    @Override
    public void export(Triangle triangle) {
        //do nothing
        System.out.println("triangle");
    }

    @Override
    public void export(Line line) {
        //do nothing
        System.out.println("line");
    }
}
class Triangle extends Shape implements Export{
    double side1;
    double side2;
    double side3;

    @Override
    void draw(double x, double y) {
        System.out.println("Drawing triangle...");
    }

    @Override
    public void export(Rectangle rectangle) {
        //do nothing
        System.out.println("rectangle");
    }

    @Override
    public void export(Circle circle) {
        //do nothing
        System.out.println("circle");
    }

    @Override
    public void export(Triangle triangle) {
        System.out.println("Exporting triangle...");
    }

    @Override
    public void export(Line line) {
        //do nothing
        System.out.println("line");
    }
}
class Line extends Shape implements Export{
    double lineLength;
    @Override
    void draw(double x, double y) {
        System.out.println("Drawing line...");
    }

    @Override
    public void export(Rectangle rectangle) {
        //do nothing
        System.out.println("rectangle");
    }

    @Override
    public void export(Circle circle) {
        //do nothing
        System.out.println("circle");
    }

    @Override
    public void export(Triangle triangle) {
        //do nothing
        System.out.println("triangle");
    }

    @Override
    public void export(Line line) {
        System.out.println("Exporting line..");
    }
}
