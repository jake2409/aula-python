public class Produtos {
    private String nome;
    private double valorUnit;
    private int qtdProdutos;
    private double imposto = 1.05;

    public String getNome() {
        return nome;
    }

    public double getValorUnit() {
        return valorUnit;
    }

    public int getQtdProdutos() {
        return qtdProdutos;
    }

    public double getImposto() {
        return imposto;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setValorUnit(double valorUnit) {
        this.valorUnit = valorUnit;
    }

    public void setQtdProdutos(int qtdProdutos) {
        this.qtdProdutos = qtdProdutos;
    }

    public void setImposto(double imposto) {
        this.imposto = imposto;
    }


    public double calculaTotal(){
        return (this.getQtdProdutos() * this.getValorUnit()) * this.getImposto();
    }
}
