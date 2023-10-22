//Polina Pushkareva
//Assignment 5 Task 1
//Decorator and Composite design patterns
import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void main(String[] args) {
        CompositeMenu mainMenu = new CompositeMenu("Main");
        CompositeMenu appetizerMenu = new CompositeMenu("Appetizer");
        CompositeMenu dessertMenu = new CompositeMenu("Dessert");
        appetizerMenu.addItem(new VegetarianDecorator(new MenuItem("Garlic bread", 5.5)));
        appetizerMenu.addItem(new SpicyDecorator(new MenuItem("Chicken wings", 12.5)));
        appetizerMenu.addItem(new VegetarianDecorator(new SpicyDecorator(new MenuItem("Tomato soup", 10.5))));
        dessertMenu.addItem(new MenuItem("Pie", 4.5));
        dessertMenu.addItem(new SpicyDecorator(new MenuItem("Pie", 4.5)));
        dessertMenu.addItem(new MenuItem("Ice cream", 3));
        mainMenu.addItem(appetizerMenu);
        mainMenu.addItem(dessertMenu);
        mainMenu.print();
    }
}
interface IMenu {
    void print();
    String getName();
    double getPrice();
}
class CompositeMenu implements IMenu {
    String name;
    List<IMenu> menuItems;
    CompositeMenu(String name) {
        this.name=name;
        menuItems=new ArrayList<>();
    }
    void addItem (IMenu iMenu) {
        menuItems.add(iMenu);
    }
    void remove (IMenu iMenu) {
        menuItems.remove(iMenu);
    }
    @Override
    public void print() {
        System.out.println(name +" Menu [$"+getPrice()+"]");
        System.out.println("----------------");
        System.out.println();
        for(IMenu menuItem : menuItems) {
            menuItem.print();
        }
        System.out.println();
    }

    @Override
    public String getName() {
        return name;
    }
    @Override
    public double getPrice() {
        double price =0;
        for(IMenu iMenu:menuItems) {
            price+=iMenu.getPrice();
        }
        return price;
    }
}
class MenuItem implements IMenu {
    String name;
    double price;
    MenuItem (String name, double price) {
        this.name=name;
        this.price=price;
    }
    @Override
    public void print() {
        System.out.println(this.name+", $"+this.price);
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double getPrice() {
        return price;
    }
}
abstract class MenuItemDecorator implements IMenu {
    IMenu menuItem;
    MenuItemDecorator(IMenu iMenu) {
        this.menuItem=iMenu;
    }
    public void print() {
        menuItem.print();
    }
}
class SpicyDecorator extends MenuItemDecorator {
    SpicyDecorator(IMenu iMenu) {
        super(iMenu);
    }
    @Override
    public void print() {
        super.print();
        //System.out.println(super.menuItem.getName()+", $"+(super.menuItem.getPrice()-2));
        System.out.println("  --This item is spicy (+$2)");
    }

    public String getName() {
        return super.menuItem.getName();
    }

    public double getPrice() {
        return super.menuItem.getPrice()+2;
    }
}
class VegetarianDecorator extends MenuItemDecorator {

    VegetarianDecorator(IMenu iMenu) {
        super(iMenu);
    }
    @Override
    public void print() {
        super.print();
        //System.out.println(super.menuItem.getName()+", $"+(super.menuItem.getPrice()-4));
        System.out.println("  --This item is vegetarian (+$4)");
    }

    public String getName() {
        return super.menuItem.getName();
    }

    public double getPrice() {
        return super.menuItem.getPrice()+4;
    }
}
