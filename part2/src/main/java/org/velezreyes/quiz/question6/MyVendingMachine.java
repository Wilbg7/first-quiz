package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class MyVendingMachine implements VendingMachine {
    private int balance;
    private Map<String, Drink> availableDrinks;

    public MyVendingMachine() {
        this.balance = 0;
        this.availableDrinks = new HashMap<>();
        
        // Agregar bebidas disponibles a la máquina
        availableDrinks.put("ScottCola", new DrinkImpl("ScottCola", true));
        availableDrinks.put("KarenTea", new DrinkImpl("KarenTea", false));
    }

    @Override
    public void insertQuarter() {
        balance += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        Drink selectedDrink = availableDrinks.get(name);

        if (selectedDrink == null) {
            throw new UnknownDrinkException();
        }

        int drinkPrice = 75; // Precio por defecto
        if (selectedDrink.getName().equals("KarenTea")) {
            drinkPrice = 100; // Precio de KarenTea
        }

        if (balance < drinkPrice) {
            throw new NotEnoughMoneyException();
        }

        balance -= drinkPrice;
        return selectedDrink;
    }
}
