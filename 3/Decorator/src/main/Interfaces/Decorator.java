package src.main.Interfaces;

public abstract class Decorator implements Beverage {
    private Beverage _beverage;

    public Decorator(Beverage _beverage) {
        this._beverage = _beverage;
    }

    @Override
    public String getDescription() {
        return _beverage.getDescription();
    }

    @Override
    public double cost() {
        return _beverage.cost();
    }
}
