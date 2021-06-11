import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Account {

    // Campo que armazena o saldo da conta
    private double balance;

    private Lock lock = new ReentrantLock();

    /**
     * Construtor da classe Account
     * 
     * @param balance
     */
    public Account(double balance) {
        this.balance = balance;
        System.out.println("Conta criada com saldo inicial de: " + balance);
    }

    /**
     * Método para realizar depósito na conta
     * 
     * @param valor
     */
    public void deposit(double valor) throws InterruptedException {
        lock.lock();

        try {
            this.balance += valor;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Méotodo para realizar saque na conta
     * 
     * @param valor
     * @return
     */
    public boolean withdraw(double valor) throws InterruptedException {
        lock.lock();

        try {
            if (this.balance < valor) {
                return false;
            } else {
                this.balance -= valor;
                return true;
            }
        } finally {
            lock.unlock();
        }
    }

    @Override
    public String toString() {
        return "Conta: saldo atualizado de " + this.balance;
    }
}
