import sys
import os
import unittest
from unittest.mock import patch

# Adiciona o diretório 'src' ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

class TestSistemaNadoLivre(unittest.TestCase):

    def setUp(self):
        """Reinicia o estado do módulo src.main antes de cada teste."""
        if 'src.main' in sys.modules:
            del sys.modules['src.main']

    def executar_sistema(self, comandos):
        """Função auxiliar para injetar comandos via input() e rodar o main."""
        input_generator = (c for c in comandos)
        
        def input_simulado(prompt=""):
            try:
                return next(input_generator)
            except StopIteration:
                return "0"

        with patch('builtins.input', side_effect=input_simulado):
            from src import main
            return main

    # ============================================================
    # 1. TESTE DE CARGA: CADASTRO DE 20 NADADORES + CONSULTAS (OPÇÃO 1)
    # ============================================================
    def test_01_cadastro_20_nadadores_e_consultas(self):
        comandos = []
        
        # Cadastra 20 nadadores (Códigos 101 a 120)
        for i in range(1, 21):
            comandos.extend(["1", "1", str(100 + i), f"Nadador {i}"])
        
        # Submenu Nadadores: Consultar todos (2), Por código (3), Por nome (4) e Voltar (0)
        comandos.extend([
            "1", "2",                 # Consultar todos
            "1", "3", "105",          # Consultar por código (105)
            "1", "4", "Nadador 15",   # Pesquisar por parte do nome
            "1", "0",                 # Voltar ao menu principal
            "0"                       # Sair do sistema
        ])
        
        main = self.executar_sistema(comandos)
        self.assertEqual(len(main.codigos), 20)
        self.assertEqual(main.nomes[4], "Nadador 5")
        self.assertEqual(main.codigos[19], 120)

    # ============================================================
    # 2. TESTE COMPLETO DE TOALHAS (OPÇÃO 2) E VALIDAÇÕES DE ESTOQUE
    # ============================================================
    def test_02_fluxo_e_validacoes_de_toalhas(self):
        comandos = [
            # Cadastra 1 nadador
            "1", "1", "101", "Arthur",
            
            # Opção 2 - Toalhas
            "2", "1", "101", "5",     # Retira 5 toalhas
            "2", "3",                 # Consulta toalhas em uso
            "2", "4",                 # Consulta estoque disponível (25 restantes)
            "2", "2", "101", "2",     # Devolve 2 toalhas (agora tem 3 em uso)
            "2", "0",                 # Voltar ao menu principal
            "0"                       # Sair
        ]
        
        main = self.executar_sistema(comandos)
        self.assertEqual(main.quantidades[0], 3)
        self.assertEqual(main.toalhas_disponiveis, 27)

    # ============================================================
    # 3. TESTE DE ÊNFASE: MOVIMENTAÇÕES E HISTÓRICO (OPÇÃO 3)
    # ============================================================
    def test_03_enfase_movimentacoes_e_historico(self):
        comandos = [
            # Cadastra 2 nadadores
            "1", "1", "101", "Arthur",
            "1", "1", "102", "Marcus",
            
            # Realiza 4 movimentações para popular o histórico
            "2", "1", "101", "4",     # Movimentação 1: Arthur retira 4
            "2", "1", "102", "2",     # Movimentação 2: Marcus retira 2
            "2", "2", "101", "1",     # Movimentação 3: Arthur devolve 1
            "2", "2", "102", "2",     # Movimentação 4: Marcus devolve 2
            "2", "0",                 # Voltar ao menu principal
            
            # --- TESTE DA OPÇÃO 3 ---
            "3", "1",                 # 3 -> 1: Consultar todas as movimentações
            "3", "2", "Arthur",       # 3 -> 2: Consultar movimentações específicas do nadador
            "3", "0",                 # Voltar
            "0"                       # Sair
        ]
        
        main = self.executar_sistema(comandos)
        
        # Validações estruturais do histórico gravado
        self.assertTrue(len(main.historico_movimentacoes) >= 4)
        
        # Garante que as movimentações de Arthur e Marcus foram registradas corretamente
        primeira_mov = main.historico_movimentacoes[0][0]
        self.assertEqual(primeira_mov[0], "Retirada")
        self.assertEqual(primeira_mov[1], 101)
        self.assertEqual(primeira_mov[2], "Arthur")
        self.assertEqual(primeira_mov[3], 4)

    # ============================================================
    # 4. TESTE DE TRATAMENTO DE ERROS E CASOS DE BORDA (ENTRADAS INVÁLIDAS)
    # ============================================================
    def test_04_tratamento_de_erros_e_validacoes(self):
        comandos = [
            "99",                     # Opção inválida no menu principal
            "1", "99",                # Opção inválida no submenu Nadadores
            "1", "1", "101", "Arthur",# Cadastra Arthur
            "1", "1", "101",          # Tenta cadastrar o mesmo código 101 (Duplicado)
            "1", "1", "102", "   ",   # Tenta cadastrar nome vazio/espaços
            "1", "1", "102", "Marcus",# Cadastra Marcus corretamente
            "2", "1", "999", "1",     # Tenta retirar toalha para código inexistente
            "2", "1", "101", "50",    # Tenta retirar mais toalhas do que o estoque total (30)
            "2", "2", "102",          # Tenta devolver de quem tem 0 toalhas
            "2", "0",                 # Voltar
            "0"                       # Sair
        ]
        
        main = self.executar_sistema(comandos)
        self.assertEqual(len(main.codigos), 2)  # Apenas Arthur e Marcus foram cadastrados

if __name__ == "__main__":
    unittest.main()