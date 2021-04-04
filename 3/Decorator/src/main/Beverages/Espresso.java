package src.main.Beverages;

import src.main.Interfaces.Beverage;

public class Espresso implements Beverage {

    public Espresso() {
    }

    @Override
    public String getDescription() {
        return "Delicious Espresso";
    }

    @Override
    public double cost() {
        return 1.99;
    }
}
