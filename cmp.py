def calcular_cmp(custo_total_atual, quantidade_atual, nova_quantidade, novo_custo_unitario):
    """
    Objectivo: Calcular o novo Custo Médio Ponderado (CMP )após uma nova compra.

    Argumentos:
        custo_total_atual (float): Custo total do stock antes da nova compra.
        quantidade_atual (int): Quantidade total de stock antes da nova compra.
        nova_quantidade (int): Quantidade de itens comprados agora.
        novo_custo_unitario (float): Custo unitário da nova compra.
    
    Retorna:
        tuple: (novo_custo_total, nova_quantidade_total, novo_cmp)
    """
    
    # 1. Calcular o custo da nova compra
    custo_da_nova_compra = nova_quantidade * novo_custo_unitario
    
    # 2. Calcular o novo custo total do inventário (Numerador da fórmula CMP)
    novo_custo_total = custo_total_atual + custo_da_nova_compra
    
    # 3. Calcular a nova quantidade total do inventário (Denominador da fórmula CMP)
    nova_quantidade_total = quantidade_atual + nova_quantidade

    # DECISÃO: Evitar divisão por zero (se o stock total for 0)
    if nova_quantidade_total == 0:
        novo_cmp = 0.0
    else:
        # 4. Calcular o Novo Custo Médio Ponderado (CMP)
        novo_cmp = novo_custo_total / nova_quantidade_total
        
    return novo_custo_total, nova_quantidade_total, novo_cmp

def main():
    # ----------------------------------------------------------------------
    # Propósito: Este script calcula o Custo Médio Ponderado (CMP) de um 
    # produto (ex: Ração para Cães) após cada nova compra, essencial para 
    # contabilidade de inventário.
    # ----------------------------------------------------------------------

    print("--- Calculadora de Custo Médio Ponderado (CMP) ---")
    
    # Variáveis de stock
    custo_total_inventario = 0.0   # O valor total que o stock custou até agora
    quantidade_total_inventario = 0  # O número total de unidades em stock
    
    # Simulação para um produto específico
    produto = input("Nome do produto a rastrear (Ex: Ração para Cães 15kg): ")
    
    continuar = True
    
    # LOOP para registar múltiplas compras
    while continuar:
        print("\n" + "="*50)
        print(f"Estado Atual do Stock de {produto}:")
        print(f"  - Quantidade Total: {quantidade_total_inventario} unidades")
        print(f"  - Custo Total: €{custo_total_inventario:.2f}")

        # Questionar o utilizador quer registar uma nova compra ou sair
        acao = input("\nRegistar **Nova Compra** (N) ou **Sair** (S)? ").strip().upper()

        if acao == 'S':
            continuar = False # Controla o loop para sair
            # break # Usando 'break' para simplicidade na interface, mas pode ser substituído por 'continuar = False'

        elif acao == 'N':
            # Solicitar os dados da nova compra
            try:
                qnt_nova = int(input(f"Quantidade de {produto} comprada (unidades): "))
                custo_novo = float(input("Custo unitário desta compra (€): "))
                
                # Validação de dados (DECISÃO)
                if qnt_nova <= 0 or custo_novo <= 0:
                    print("Por favor, insira valores positivos para a quantidade e custo.")
                    continue

                # Função Auxiliar: Calcular o novo CMP
                custo_total_inventario, quantidade_total_inventario, novo_cmp = calcular_cmp(
                    custo_total_inventario, 
                    quantidade_total_inventario, 
                    qnt_nova, 
                    custo_novo
                )
                
                # Apresentação dos resultados
                print("\n**--- REGISTO DE COMPRA CONCLUÍDO ---**")
                print(f"  - Nova Quantidade Total em Stock: {quantidade_total_inventario} unidades")
                print(f"  - Novo Custo Médio Ponderado (CMP): **€{novo_cmp:.2f}**")
                print("---------------------------------------")
            
            except ValueError:
                print("ERRO: Por favor, insira apenas números válidos para quantidade e custo.")

        else:
            print("Opção inválida. Por favor, digite 'N' para Nova Compra ou 'S' para Sair.")

    print("\n--- Simulação de CMP Finalizada. ---")
    print(f"O Custo Médio Ponderado final de {produto} é: **€{novo_cmp:.2f}**")


if __name__ == "__main__":
    main()
