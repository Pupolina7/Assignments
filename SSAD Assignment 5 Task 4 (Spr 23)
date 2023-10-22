//Polina Pushkareva
//Assignment 5 Task 4
//Iterator design pattern
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        Shop groceryShop = new Shop();
        groceryShop.add("bread", 10);
        groceryShop.add("milk", 20);
        groceryShop.add("apples", 16);
        groceryShop.add("lemon", 1);
        System.out.println("Grocery shop list:");
        groceryShop.print();
        ShopList customer1 = new ShopList();
        customer1.addItem(new ShopItem("lemon", 1));
        customer1.addItem(new ShopItem("bread", 1));
        System.out.println("Customer 1 list:");
        customer1.print();
        Iterator iterator = customer1.getIterator();
        while (iterator.hasNext()) {
            groceryShop.buy((ShopItem) iterator.next());
        }
        System.out.println("Updated grocery shop list:");
        groceryShop.print();
        ShopList customer2 = new ShopList();
        customer2.addItem(new ShopItem("milk", 5));
        customer2.addItem(new ShopItem("bread", 3));
        System.out.println("Customer 2 list:");
        customer2.print();
        iterator = customer2.getIterator();
        while (iterator.hasNext()) {
            groceryShop.buy((ShopItem) iterator.next());
        }
        System.out.println("Updated grocery shop list:");
        groceryShop.print();
        ShopList customer3 = new ShopList();
        customer3.addItem(new ShopItem("lemon", 1));
        customer3.addItem(new ShopItem("apples", 20));
        System.out.println("Customer 3 list:");
        customer3.print();
        iterator = customer3.getIterator();
        while (iterator.hasNext()) {
            groceryShop.buy((ShopItem) iterator.next());
        }
        System.out.println("Updated grocery shop list:");
        groceryShop.print();
    }
}
interface Iterator {
    boolean hasNext();
    Object next() throws IOException;
}
class ShopItem {
    private final String name;
    private int quantity;

    public ShopItem(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public void decreaseQuantity(int amount) {
        quantity -= amount;
    }

    @Override
    public String toString() {
        return name + ", " + quantity;
    }
}

class Shop {
    private String file = "shop.txt";
    private boolean loaded;
    private List<ShopItem> shopItems;
    public Shop() {
        loaded=false;
        shopItems = new ArrayList<>();
    }
    void add(String name, int quantity) {
        shopItems.add(new ShopItem(name, quantity));
    }
    //lazy loading
    private void load() throws IOException {
        if (!loaded) {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line;
            int count = 0;
            while ((line = reader.readLine()) != null) {
                count++;
            }
            reader.close();
            reader = new BufferedReader(new FileReader(file));
            //shopItems = new ShopItem[count];
            int i = 0;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                String name = parts[0].trim().substring(1);
                int quantity = Integer.parseInt(parts[1].trim().substring(0, parts[1].trim().length() - 1));
                shopItems.set(i, new ShopItem(name, quantity));
                i++;
            }
            reader.close();
            loaded = true;
        }
    }
    public ShopItem find(ShopItem item) throws IOException {
        //load();
        for(ShopItem shopItem : shopItems) {
            if(shopItem.getName().equals(item.getName())) {
                return shopItem;
            }
        }
        return null;
    }
    public void buy(ShopItem shopItem) throws IOException {
        ShopItem item = find(shopItem);
        if (item != null) {
            if (item.getQuantity() >= shopItem.getQuantity()) {
                item.decreaseQuantity(shopItem.getQuantity());
                if(item.getQuantity()==0) {
                    shopItems.remove(item);
                }
            } else {
                System.out.println("Sorry, you can buy only "+item.getQuantity()+ " "+ item.getName()+"\n");
                shopItems.remove(item);
            }
        } else {
            System.out.println("Sorry, "+shopItem.getName()+" is/are not available\n");
        }
    }
    void print() {
        for(ShopItem shopItem:shopItems) {
            System.out.println(shopItem.toString());
        }
        System.out.println();
    }

}
class ShopList {
    private List<ShopItem> shopItems =  new ArrayList<>();
    public void addItem(ShopItem item) {
        shopItems.add(item);
    }
    public void iterate (Shop shop) {
        for(ShopItem shopItem: shopItems) {

        }
    }
    public Iterator getIterator() {
        return new ShopIterator();
    }
    void print() {
        for(ShopItem shopItem:shopItems) {
            System.out.println(shopItem.toString());
        }
        System.out.println();
    }
    class ShopIterator implements Iterator {
        private int index;
        public ShopIterator() {
            this.index=0;
        }

        @Override
        public boolean hasNext() {
            return index<shopItems.size();
        }

        @Override
        public Object next() throws IOException {
            if(hasNext()) {
                ShopItem item = shopItems.get(index);
                index++;
                return item;
            }
            return null;
        }
    }
}

