"""
Testes para src/main.py (Sistema de Controle de Toalhas - NADO LIVRE).

Como rodar (na raiz do projeto):
    pip install pytest
    pytest -v
"""
import sys
from pathlib import Path

import pytest

# Permite importar src/main.py a partir da pasta tests/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import main  # noqa: E402


# ------------------------------------------------------------
# HELPERS E FIXTURES
# ------------------------------------------------------------

def simular_entradas(monkeypatch, *valores):
    """Substitui input() por uma sequência de respostas pré-definidas."""
    it = iter(valores)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))


def cadastrar(codigo, nome="Fulano", toalha=0):
    """Atalho para inserir um nadador direto na lista (sem passar pelo menu)."""
    nadador = {"codigo": codigo, "nome": nome, "toalha": toalha}
    main.nadadores.append(nadador)
    return nadador


@pytest.fixture(autouse=True)
def resetar_estado():
    """Garante que cada teste comece com o estado global limpo."""
    main.nadadores.clear()
    main.historico_movimentacoes.clear()
    main.toalhas_disponiveis = main.TOTAL_TOALHAS
    yield
    main.nadadores.clear()
    main.historico_movimentacoes.clear()
    main.toalhas_disponiveis = main.TOTAL_TOALHAS


# ------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ------------------------------------------------------------

class TestSolicitarOpcaoMenu:
    @pytest.mark.parametrize("entrada, esperado", [
        ("1", 1),
        ("0", 0),
        (" 3 ", 3),
        ("abc", -1),
        ("-1", -1),
        ("1.5", -1),
        ("", -1),
    ])
    def test_opcoes(self, monkeypatch, entrada, esperado):
        simular_entradas(monkeypatch, entrada)
        assert main.solicitar_opcao_menu() == esperado


class TestSolicitarCodigo:
    def test_codigo_valido(self, monkeypatch):
        simular_entradas(monkeypatch, "15")
        assert main.solicitar_codigo() == 15

    def test_codigo_nao_numerico(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "abc")
        assert main.solicitar_codigo() is None
        assert "Código inválido" in capsys.readouterr().out

    def test_codigo_negativo(self, monkeypatch):
        simular_entradas(monkeypatch, "-5")
        assert main.solicitar_codigo() is None

    def test_codigo_zero(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "0")
        assert main.solicitar_codigo() is None
        assert "maior que zero" in capsys.readouterr().out


class TestSolicitarQuantidade:
    def test_quantidade_valida(self, monkeypatch):
        simular_entradas(monkeypatch, "4")
        assert main.solicitar_quantidade("Qtd: ") == 4

    def test_quantidade_nao_numerica(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "x")
        assert main.solicitar_quantidade("Qtd: ") is None
        assert "Quantidade inválida" in capsys.readouterr().out

    def test_quantidade_zero(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "0")
        assert main.solicitar_quantidade("Qtd: ") is None
        assert "maior que zero" in capsys.readouterr().out


class TestBuscarNadador:
    def test_encontra_nadador(self):
        n = cadastrar(1, "Ana")
        assert main.buscar_nadador_por_codigo(1) is n

    def test_nao_encontra_nadador(self):
        cadastrar(1, "Ana")
        assert main.buscar_nadador_por_codigo(99) is None

    def test_lista_vazia(self):
        assert main.buscar_nadador_por_codigo(1) is None


class TestRegistrarMovimentacao:
    def test_registra_dados_corretos(self):
        n = cadastrar(1, "Ana")
        main.registrar_movimentacao(n, 3, "Retirada")
        assert main.historico_movimentacoes == [
            {"codigo": 1, "nome": "Ana", "toalha": 3, "acao": "Retirada"}
        ]


# ------------------------------------------------------------
# NADADORES
# ------------------------------------------------------------

class TestCadastroNadador:
    def test_cadastro_sucesso(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "1", "joão silva")
        main.cadastro_nadador()

        assert main.nadadores == [{"codigo": 1, "nome": "João Silva", "toalha": 0}]
        assert "cadastrado com sucesso" in capsys.readouterr().out

    def test_codigo_duplicado(self, monkeypatch, capsys):
        cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1")
        main.cadastro_nadador()

        assert len(main.nadadores) == 1
        assert "já cadastrado" in capsys.readouterr().out

    def test_nome_vazio(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "1", "   ")
        main.cadastro_nadador()

        assert main.nadadores == []
        assert "nome não pode ser vazio" in capsys.readouterr().out

    def test_codigo_invalido_nao_cadastra(self, monkeypatch):
        simular_entradas(monkeypatch, "abc")
        main.cadastro_nadador()
        assert main.nadadores == []


class TestListarNadadores:
    def test_lista_vazia(self, capsys):
        main.listar_nadadores()
        assert "Nenhum nadador cadastrado" in capsys.readouterr().out

    def test_lista_com_nadadores(self, capsys):
        cadastrar(1, "Ana")
        cadastrar(2, "Bruno")
        main.listar_nadadores()
        saida = capsys.readouterr().out
        assert "Ana" in saida and "Bruno" in saida


class TestConsultarNadadores:
    def test_encontrado(self, monkeypatch, capsys):
        cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1")
        main.consultar_nadadores()
        saida = capsys.readouterr().out
        assert "Nadador encontrado" in saida and "Ana" in saida

    def test_nao_encontrado(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "7")
        main.consultar_nadadores()
        assert "não encontrado" in capsys.readouterr().out


class TestPesquisarNadadores:
    def test_busca_parcial_sem_diferenciar_maiusculas(self, monkeypatch, capsys):
        cadastrar(1, "Maria Souza")
        cadastrar(2, "Mario Lima")
        cadastrar(3, "Pedro")
        simular_entradas(monkeypatch, "MAR")
        main.pesquisar_nadadores()
        saida = capsys.readouterr().out
        assert "Nadadores encontrados" in saida
        assert "Maria Souza" in saida and "Mario Lima" in saida
        assert "Pedro" not in saida

    def test_um_resultado_usa_singular(self, monkeypatch, capsys):
        cadastrar(1, "Maria Souza")
        simular_entradas(monkeypatch, "souza")
        main.pesquisar_nadadores()
        assert "Nadador encontrado" in capsys.readouterr().out

    def test_sem_resultados(self, monkeypatch, capsys):
        cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "zzz")
        main.pesquisar_nadadores()
        assert "Nenhum nadador encontrado" in capsys.readouterr().out


# ------------------------------------------------------------
# TOALHAS
# ------------------------------------------------------------

class TestRetiradaToalhas:
    def test_retirada_sucesso(self, monkeypatch, capsys):
        n = cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1", "5")
        main.submenu_retirada_toalhas()

        assert n["toalha"] == 5
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS - 5
        assert main.historico_movimentacoes[-1] == {
            "codigo": 1, "nome": "Ana", "toalha": 5, "acao": "Retirada"
        }
        assert "Retirada registrada com sucesso" in capsys.readouterr().out

    def test_codigo_inexistente(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "99")
        main.submenu_retirada_toalhas()

        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS
        assert main.historico_movimentacoes == []
        assert "não encontrado" in capsys.readouterr().out

    def test_quantidade_invalida(self, monkeypatch):
        n = cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1", "0")
        main.submenu_retirada_toalhas()

        assert n["toalha"] == 0
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS

    def test_estoque_insuficiente(self, monkeypatch, capsys):
        n = cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1", str(main.TOTAL_TOALHAS + 1))
        main.submenu_retirada_toalhas()

        assert n["toalha"] == 0
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS
        assert main.historico_movimentacoes == []
        assert "Estoque insuficiente" in capsys.readouterr().out

    def test_retira_exatamente_todo_o_estoque(self, monkeypatch):
        n = cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1", str(main.TOTAL_TOALHAS))
        main.submenu_retirada_toalhas()

        assert n["toalha"] == main.TOTAL_TOALHAS
        assert main.toalhas_disponiveis == 0


class TestDevolucaoToalhas:
    def test_devolucao_sucesso(self, monkeypatch, capsys):
        n = cadastrar(1, "Ana", toalha=5)
        main.toalhas_disponiveis = main.TOTAL_TOALHAS - 5
        simular_entradas(monkeypatch, "1", "2")
        main.submenu_devolucao_toalhas()

        assert n["toalha"] == 3
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS - 3
        assert main.historico_movimentacoes[-1]["acao"] == "Devolução"
        assert "Devolução registrada com sucesso" in capsys.readouterr().out

    def test_codigo_inexistente(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "99")
        main.submenu_devolucao_toalhas()
        assert "não encontrado" in capsys.readouterr().out

    def test_nadador_sem_toalhas(self, monkeypatch, capsys):
        cadastrar(1, "Ana", toalha=0)
        simular_entradas(monkeypatch, "1")
        main.submenu_devolucao_toalhas()

        assert "não possui toalhas para devolver" in capsys.readouterr().out
        assert main.historico_movimentacoes == []

    def test_devolve_mais_do_que_possui(self, monkeypatch, capsys):
        n = cadastrar(1, "Ana", toalha=2)
        main.toalhas_disponiveis = main.TOTAL_TOALHAS - 2
        simular_entradas(monkeypatch, "1", "5")
        main.submenu_devolucao_toalhas()

        assert n["toalha"] == 2
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS - 2
        assert "possui apenas 2" in capsys.readouterr().out

    def test_quantidade_invalida(self, monkeypatch):
        n = cadastrar(1, "Ana", toalha=2)
        simular_entradas(monkeypatch, "1", "abc")
        main.submenu_devolucao_toalhas()
        assert n["toalha"] == 2


class TestToalhasEmUsoEEstoque:
    def test_em_uso_sem_ninguem(self, capsys):
        cadastrar(1, "Ana", toalha=0)
        main.toalhas_em_uso()
        assert "Nenhum nadador está com toalhas" in capsys.readouterr().out

    def test_em_uso_lista_apenas_quem_tem_toalha(self, capsys):
        cadastrar(1, "Ana", toalha=2)
        cadastrar(2, "Bruno", toalha=0)
        main.toalhas_em_uso()
        saida = capsys.readouterr().out
        assert "Ana" in saida
        assert "Bruno" not in saida

    def test_consulta_estoque(self, capsys):
        main.toalhas_disponiveis = 12
        main.consulta_toalhas()
        assert f"12 de {main.TOTAL_TOALHAS}" in capsys.readouterr().out


# ------------------------------------------------------------
# MOVIMENTAÇÕES
# ------------------------------------------------------------

class TestMovimentacoes:
    def test_historico_vazio(self, capsys):
        main.consultar_movimentacoes()
        assert "Nenhuma movimentação registrada" in capsys.readouterr().out

    def test_lista_historico(self, capsys):
        a = cadastrar(1, "Ana")
        main.registrar_movimentacao(a, 2, "Retirada")
        main.registrar_movimentacao(a, 1, "Devolução")
        main.consultar_movimentacoes()
        saida = capsys.readouterr().out
        assert "Retirada" in saida and "Devolução" in saida

    def test_movimentacoes_por_nadador_mantem_ordem_original(self, monkeypatch, capsys):
        a = cadastrar(1, "Ana")
        b = cadastrar(2, "Bruno")
        main.registrar_movimentacao(a, 2, "Retirada")   # ordem 1
        main.registrar_movimentacao(b, 3, "Retirada")   # ordem 2
        main.registrar_movimentacao(a, 1, "Devolução")  # ordem 3
        simular_entradas(monkeypatch, "1")
        main.consultar_movimentacoes_nadadores()

        linhas = [l for l in capsys.readouterr().out.splitlines()
                  if "Retirada" in l or "Devolução" in l]
        assert len(linhas) == 2
        assert linhas[0].startswith("1")
        assert linhas[1].startswith("3")
        assert all("Bruno" not in l for l in linhas)

    def test_movimentacoes_nadador_sem_historico(self, monkeypatch, capsys):
        cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1")
        main.consultar_movimentacoes_nadadores()
        assert "Nenhuma movimentação encontrada" in capsys.readouterr().out


# ------------------------------------------------------------
# MENUS (navegação)
# ------------------------------------------------------------

class TestMenus:
    def test_menu_nadadores_cadastra_e_volta(self, monkeypatch):
        simular_entradas(monkeypatch, "1", "10", "joão silva", "0")
        main.menu_nadadores()
        assert main.nadadores[0]["nome"] == "João Silva"

    def test_menu_nadadores_opcao_invalida(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "9", "0")
        main.menu_nadadores()
        assert "Opção inválida" in capsys.readouterr().out

    def test_menu_toalhas_fluxo_retirada(self, monkeypatch):
        n = cadastrar(1, "Ana")
        simular_entradas(monkeypatch, "1", "1", "3", "0")
        main.menu_toalhas()
        assert n["toalha"] == 3

    def test_menu_toalhas_opcao_invalida(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "abc", "0")
        main.menu_toalhas()
        assert "Opção inválida" in capsys.readouterr().out

    def test_menu_movimentacoes_opcao_invalida(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "7", "0")
        main.menu_movimentacoes()
        assert "Opção inválida" in capsys.readouterr().out

    def test_programa_principal_sai_com_zero(self, monkeypatch, capsys):
        # Requer a função main() (veja a refatoração com if __name__ == "__main__")
        simular_entradas(monkeypatch, "0")
        main.main()
        assert "Saindo do sistema" in capsys.readouterr().out

    def test_programa_principal_opcao_invalida(self, monkeypatch, capsys):
        simular_entradas(monkeypatch, "9", "0")
        main.main()
        assert "Opção inválida" in capsys.readouterr().out


# ------------------------------------------------------------
# INTEGRAÇÃO
# ------------------------------------------------------------

class TestFluxoCompleto:
    def test_retirada_e_devolucao_restauram_estoque(self, monkeypatch):
        n = cadastrar(1, "Ana")

        simular_entradas(monkeypatch, "1", "10")
        main.submenu_retirada_toalhas()
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS - 10

        simular_entradas(monkeypatch, "1", "10")
        main.submenu_devolucao_toalhas()

        assert n["toalha"] == 0
        assert main.toalhas_disponiveis == main.TOTAL_TOALHAS
        assert [m["acao"] for m in main.historico_movimentacoes] == ["Retirada", "Devolução"]

    def test_estoque_total_sempre_consistente(self, monkeypatch):
        a = cadastrar(1, "Ana")
        b = cadastrar(2, "Bruno")

        simular_entradas(monkeypatch, "1", "7")
        main.submenu_retirada_toalhas()
        simular_entradas(monkeypatch, "2", "8")
        main.submenu_retirada_toalhas()
        simular_entradas(monkeypatch, "1", "3")
        main.submenu_devolucao_toalhas()

        em_uso = a["toalha"] + b["toalha"]
        assert em_uso + main.toalhas_disponiveis == main.TOTAL_TOALHAS