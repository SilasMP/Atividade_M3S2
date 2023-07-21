
def decorador_imprimir(funcao):
    def gerador_resultado(*args):
        resultado = funcao(*args)
        print(f'CAPITAL: {args[0]} TAXA: {args[1]} TEMPO: {args[2]}')        
        return print(f'RESULTADO: {resultado}')
    return gerador_resultado

@decorador_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_simples(1000, 5, 6)