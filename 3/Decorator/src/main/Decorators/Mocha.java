package src.main.Decorators;

import src.main.Interfaces.Beverage;
import src.main.Interfaces.Decorator;

public class Mocha extends Decorator {

    public Mocha(Beverage _beverage) {
        super(_beverage);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with mocha";
    }

    @Override
    public double cost() {
        return super.cost() + 0.2;
    }
}
