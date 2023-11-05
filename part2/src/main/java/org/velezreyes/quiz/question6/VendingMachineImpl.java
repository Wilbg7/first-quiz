package org.velezreyes.quiz.question6;

public class VendingMachineImpl {
    private static VendingMachine instance;

    public static VendingMachine getInstance() {
        if (instance == null) {
            instance = new MyVendingMachine();
        }
        return instance;
    }
}
