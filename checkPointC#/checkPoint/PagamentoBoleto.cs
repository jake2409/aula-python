﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace checkPoint
{
    internal class PagamentoBoleto : PagamentoInterface
    {
        public double value { get; set; }
        public int number { get; set; }

        public override void ProcessaPagamento()
        {
            Console.WriteLine("Informe o número do código de barras: ");
            string codBarras = Console.ReadLine();

            Console.WriteLine("Informe o valor a ser processado: ");
            string valor = Console.ReadLine();

            try
            {
                number = int.Parse(codBarras);
                value = double.Parse(valor);

                Console.WriteLine($"Processando o pagamento de R$ {value} via boleto (cod barras: {number}) na data {DateTime.Now.ToString("dd/MM/yyyy")}");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Não foi possivel converter o valor informado");
            }
        }
    }
}
