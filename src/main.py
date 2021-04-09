from matplotlib import pyplot
import numpy

# ------------

NUMERO_AMOSTRAS = 500
TAXA_DE_SIMBOLO = 100
NUMERO_DE_SIMBOLO = NUMERO_AMOSTRAS / TAXA_DE_SIMBOLO


def pulso_conformador(taxa_simbolo: int):
    meio = int(taxa_simbolo / 2)
    pShaping = numpy.ones((1, taxa_simbolo), dtype=int)
    pShaping[0, meio:] = 0
    return pShaping[0]


def sinal_sequencia_de_bits(numero_amostras: int, taxa_de_simbolo: int):
    """
    Cria sequência de bits
    """
    numero_de_simbolo = numero_amostras / taxa_de_simbolo

    sinal_senquencia_bits = 2 * (
        numpy.random.randint(1, 3, size=int(numero_de_simbolo)) - 1.5
    )  # Função do Sinal de sequência de Bits
    return (sinal_senquencia_bits + 1) / 2


def sinal_digital(pulso_conformador, sequencia_de_bits, numero_simbolos):
    sinal_digital = []
    for s in range(0, int(numero_simbolos)):
        sinal_auxiliar = sequencia_de_bits[s] * pulso_conformador
        for k in range(0, len(sinal_auxiliar)):
            sinal_digital.append(sinal_auxiliar[k])

    return sinal_digital


sinal_pulso_conformador = pulso_conformador(TAXA_DE_SIMBOLO)

sequencia_de_bits = sinal_sequencia_de_bits(NUMERO_AMOSTRAS, TAXA_DE_SIMBOLO)
rz_unipolar = sinal_digital(
    sinal_pulso_conformador, sequencia_de_bits, NUMERO_DE_SIMBOLO
)
figura, (grafico_1, grafico_2) = pyplot.subplots(2, 1)

grafico_1.stem(
    sequencia_de_bits,
    use_line_collection=True,
)
grafico_2.plot(rz_unipolar, ".-")
pyplot.show()
