package src.main.Beverages;

import src.main.Interfaces.Beverage;

public class HouseBlend implements Beverage {

    public HouseBlend() {
    }

    @Override
    public String getDescription() {
        return "Delicious HouseBlend";
    }

    @Override
    public double cost() {
        return 0.89;
    }
}
