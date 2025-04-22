using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace checkPoint
{
    internal class Menu
    {
        public static void ExibirMenu()
        {
            Console.WriteLine("1 - Cartão\r\n2 - Boleto\r\n3 - Sair\r\nEscolha uma opção: ");
            string opcao = Console.ReadLine();
            string[] opcoes = {"1", "2", "3"};
            if(!opcoes.Contains(opcao))
            {
                Console.WriteLine("Opção não existente! Escolha uma opção dentre as informadas.");
                Menu.ExibirMenu();
            }

            switch(opcao)
            {
                case "1": 
                    Console.WriteLine("Escolheu a pagamento com cartão");
                    PagamentoCartao pagCartao = new PagamentoCartao();
                    pagCartao.ProcessaPagamento();
                    break;
                case "2":
                    Console.WriteLine("Escolheu pagamento com boleto");
                    PagamentoBoleto pagBoleto = new PagamentoBoleto();
                    pagBoleto.ProcessaPagamento();
                    break;
                case "3": 
                    Console.WriteLine("Escolheu a opção sair. Obrigado por usar o nosso sistema.");
                    Environment.Exit(0);
                    break;
            }
            Menu.ExibirMenu();

        }
    }
}
