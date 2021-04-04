package src.main.Decorators;

import src.main.Interfaces.Beverage;
import src.main.Interfaces.Decorator;

public class Whip extends Decorator {

    public Whip(Beverage _beverage) {
        super(_beverage);
    }

    @Override
    public String getDescription() {
        return null;
    }

    @Override
    public double cost() {
        return 0;
    }
}
