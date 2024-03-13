// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Produtos prdtOculos = new Produtos();
        prdtOculos.setNome("Oculos");
        prdtOculos.setValorUnit(30.00);
        prdtOculos.setQtdProdutos(3);
        double totOculos = prdtOculos.calculaTotal();

        Produtos prdtRelogio = new Produtos();
        prdtRelogio.setNome("Relogio");
        prdtRelogio.setValorUnit(15000.00);
        prdtRelogio.setQtdProdutos(1);
        double totRelogio = prdtRelogio.calculaTotal();

        Produtos prdtTenis = new Produtos();
        prdtTenis.setNome("Tenis");
        prdtTenis.setValorUnit(300.00);
        prdtTenis.setQtdProdutos(1);
        double totTenis = prdtTenis.calculaTotal();

        Produtos prdtCamiseta = new Produtos();
        prdtCamiseta.setNome("Camiseta");
        prdtCamiseta.setValorUnit(100.00);
        prdtCamiseta.setQtdProdutos(1);
        double totCamiseta = prdtCamiseta.calculaTotal();

        String mensgem = "Você comprou: \n" +
                prdtOculos.getNome() + " R$" + totOculos + "\n" +
                prdtRelogio.getNome() + " R$" + totRelogio + "\n" +
                prdtTenis.getNome() + " R$" + totTenis + "\n" +
                prdtCamiseta.getNome() + " R$" + totCamiseta;

        System.out.println(mensgem);
    }
}