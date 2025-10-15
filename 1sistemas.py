public class Main {
    public static void main(String[] args) {
        int idade = 25;
        double salario = 3500.50;
        double altura = 1.75;
        double peso = 70.5;
        String nome = "Jamal";
        String genero = "m";

        System.out.println("A pessoa é maior de idade: " + (idade >= 18));
        System.out.println("Ganha mais que o salário mínimo: " + (salario > 1212));
        System.out.println("A altura é maior que 1.8m: " + (altura > 1.8));
        System.out.println("O peso é menor que 60kg: " + (peso < 60));
        System.out.println("O nome é igual ao meu: " + nome.equalsIgnoreCase("jamal"));
        System.out.println("O gênero é igual a 'm': " + genero.equalsIgnoreCase("m"));
    }
}