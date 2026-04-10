from colorama import Fore, Back, Style, init
from estruturas import fila_espera, lista_pousados, pilha_alerta
from busca_ordenacao import *
from autorizacao import autorizar_pouso

# Inicializa o colorama com autoreset
init(autoreset=True)


def desenhar_divisor(estilo="normal"):
    cor_borda = Fore.MAGENTA
    if estilo == "duplo":
        print(cor_borda + "═" * 110)
    elif estilo == "header":
        print(cor_borda + "╔" + "═" * 108 + "╗")
    elif estilo == "footer":
        print(cor_borda + "╚" + "═" * 108 + "╝")
    else:
        print(cor_borda + "─" * 110)


def painel_titulo(texto):
    print("\n")
    desenhar_divisor("header")
    print(
        Fore.MAGENTA
        + "║"
        + Style.BRIGHT
        + Fore.YELLOW
        + f" {texto.center(106)} "
        + Fore.MAGENTA
        + "║"
    )
    desenhar_divisor("footer")


def exibir_cabecalho():
    print(
        Fore.MAGENTA
        + Style.BRIGHT
        + """
    ░█████╗░██╗░░░██╗██████╗░░█████╗░██████╗░░█████╗░  ░██████╗██╗░██████╗░███████╗██████╗░
    ██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██║██╔════╝░██╔════╝██╔══██╗
    ███████║██║░░░██║██████╔╝██║░░██║██████╔╝███████║  ╚█████╗░██║██║░░██╗░█████╗░░██████╔╝
    ██╔══██║██║░░░██║██╔══██╗██║░░██║██╔══██╗██╔══██║  ░╚═══██╗██║██║░░╚██╗██╔══╝░░██╔══██╗
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║  ██████╔╝██║╚██████╔╝███████╗██║░░██║
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝
    """
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "       MÓDULO DE GERENCIAMENTO DE POUSO E ESTABILIZAÇÃO DE BASE (MGPEB) - MISSÃO AURORA SIGER".center(
            110
        )
    )
    print("\n")


def exibir_modulos_fila_inicial():
    painel_titulo("FILA INICIAL DE MÓDULOS EM ÓRBITA")

    header = f" {'NOME':<12} │ {'TIPO':<15} │ {'PRIO':<5} │ {'COMB':<6} │ {'MASSA':<8} │ {'CRIT':<5} │ {'CHEGADA':<10} │ {'SENSORES':<10} │ {'ÁREA':<6}"
    print(Fore.CYAN + Style.BRIGHT + header)
    print(Fore.MAGENTA + "─" * 110)

    for m in fila_espera:
        # Sensores e Área: Ciano para OK, Amarelo para Alerta/Falha
        sensor_status = Fore.CYAN + "OK" if m["sensor_ok"] else Fore.YELLOW + "FALHA"
        area_status = Fore.CYAN + "LIVRE" if m["area_livre"] else Fore.YELLOW + "OCUP."

        # Combustível: Ciano para seguro, Amarelo para atenção, Magenta para crítico
        if m["combustivel"] > 50:
            comb_cor = Fore.CYAN
        elif m["combustivel"] > 25:
            comb_cor = Fore.YELLOW
        else:
            comb_cor = Fore.MAGENTA

        row = (
            f" {Fore.CYAN}{m['nome']:<12}{Fore.MAGENTA} │ "
            f"{Fore.MAGENTA}{m['tipo']:<15}{Fore.MAGENTA} │ "
            f"{Fore.CYAN}{m['prioridade']:<5}{Fore.MAGENTA} │ "
            f"{comb_cor}{m['combustivel']:>4}%" + Fore.MAGENTA + "  │ "
            f"{Fore.CYAN}{m['massa']:>6}t  {Fore.MAGENTA}│ "
            f"{Fore.CYAN}{m['criticidade']:^5} {Fore.MAGENTA}│ "
            f"{Fore.CYAN}{m['hora_chegada']:>8}h {Fore.MAGENTA}│ "
            f"{sensor_status:<19} {Fore.MAGENTA}│ "
            f"{area_status}"
        )
        print(row)
    desenhar_divisor()


def exibir_fila_ordenada(fila):
    painel_titulo("REORGANIZAÇÃO DA FILA POR PRIORIDADE")

    fila_ordenada = bubble_sort_prioridade(list(fila))

    for m in fila_ordenada:
        print(
            Fore.MAGENTA
            + "  [►] "
            + Fore.CYAN
            + f"{m['nome']:<12} "
            + Fore.MAGENTA
            + "│ "
            + Fore.YELLOW
            + f"Prioridade: {m['prioridade']}"
        )

    desenhar_divisor()
    return fila_ordenada


def processar_pousos(fila):
    painel_titulo("SEQUÊNCIA DE POUSO E ESTABILIZAÇÃO")

    while fila:
        modulo = fila.pop(0)
        status = autorizar_pouso(modulo)

        if status == "POUSO AUTORIZADO":
            lista_pousados.append(modulo)
            cor = Fore.CYAN
            ícone = "✔"
        elif status == "ALERTA":
            pilha_alerta.append(modulo)
            cor = Fore.YELLOW
            ícone = "⚠"
        else:
            cor = Fore.MAGENTA
            ícone = "✖"

        print(
            f" {Fore.MAGENTA}║ {Fore.CYAN}{modulo['nome']:<12} {Fore.MAGENTA}→ {cor}{ícone} {status:<20}"
        )

    desenhar_divisor("footer")


def exibir_resultados():
    painel_titulo("STATUS FINAL DA OPERAÇÃO")

    print(Fore.CYAN + Style.BRIGHT + "  MÓDULOS POUSADOS COM SUCESSO:")
    if not lista_pousados:
        print(Fore.MAGENTA + "  (Nenhum)")
    for m in lista_pousados:
        print(f"  {Fore.CYAN}● {Fore.CYAN}{m['nome']} ({m['tipo']})")

    print("\n" + Fore.YELLOW + Style.BRIGHT + "  MÓDULOS EM ESTADO DE ALERTA:")
    if not pilha_alerta:
        print(Fore.MAGENTA + "  (Nenhum)")
    for m in pilha_alerta:
        print(f"  {Fore.YELLOW}▲ {Fore.YELLOW}{m['nome']} ({m['tipo']})")

    desenhar_divisor("footer")


def exibir_buscas(fila):
    painel_titulo("RELATÓRIO DE BUSCA E TELEMETRIA")

    menor = buscar_menor_combustivel(fila)
    # Destaque para o valor crítico em Amarelo
    print(
        f"  {Fore.MAGENTA}» {Fore.CYAN}Crítico (Menor Combustível): {Fore.YELLOW}{menor['nome']} ({menor['combustivel']}%)"
    )

    habitacao = buscar_por_tipo(fila, "Habitação")
    for h in habitacao:
        print(f"  {Fore.MAGENTA}» {Fore.CYAN}Módulo de Habitação: {Fore.YELLOW}{h['nome']} ({h['tipo']})")

    desenhar_divisor()
