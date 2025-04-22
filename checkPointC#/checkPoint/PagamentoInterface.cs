using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace checkPoint
{
    public abstract class PagamentoInterface
    {
        public double value { get; set; }
        public int number { get; set; }

        public abstract void ProcessaPagamento();
    }
}
