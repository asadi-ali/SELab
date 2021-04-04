package src.main.Decorators;

import src.main.Interfaces.Beverage;
import src.main.Interfaces.Decorator;

public class SteamedMilk extends Decorator {

    public SteamedMilk(Beverage _beverage) {
        super(_beverage);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with milk";
    }

    @Override
    public double cost() {
        return super.cost() + 0.1;
    }
}
