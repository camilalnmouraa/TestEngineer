import threading
import time
import pytest
import numpy as np

@pytest.fixture
def sample_obj_definition():
    """
    Fixture que fornece uma definição de objeto retangular de exemplo.
    """
    return {'top': 10, 'left': 20, 'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0}

@pytest.fixture
def sample_dsize():
    """
    Fixture que fornece um tamanho de imagem de exemplo.
    """
    return (100, 100)

@pytest.fixture
def sample_frame_affine_matrix():
    """
    Fixture que fornece uma matriz de transformação afim de exemplo.
    """
    return np.identity(3)

@pytest.fixture
def sample_edge_locs():
    """
    Fixture que fornece uma lista de locais de borda de exemplo.
    """
    return [(10, 10), (20, 20)]

@pytest.fixture
def sample_color():
    """
    Fixture que fornece uma cor de exemplo no formato BGR.
    """
    return (0, 0, 255)

@pytest.fixture
def sample_hex_color():
    """
    Fixture que fornece uma cor de exemplo no formato hexadecimal.
    """
    return '#FF0000'

@pytest.fixture
def sample_bgr_color():
    """
    Fixture que fornece uma cor de exemplo no formato BGR.
    """
    return (0, 0, 255)

# Definindo fixtures para dados adicionais de exemplo

@pytest.fixture
def additional_obj_definitions():
    """
    Fixture que fornece uma lista de definições de objeto retangular adicionais de exemplo.
    """
    return [
        {'top': 50, 'left': 60, 'width': 70, 'height': 80, 'scaleX': 1.5, 'scaleY': 1.5, 'angle': 90},
        {'top': 20, 'left': 30, 'width': 40, 'height': 50, 'scaleX': 2, 'scaleY': 2, 'angle': 180},
    ]

@pytest.fixture
def additional_frame_affine_matrices():
    """
    Fixture que fornece uma lista de matrizes de transformação afim adicionais de exemplo.
    """
    return [
        np.array([[1, 0, 10], [0, 1, 20], [0, 0, 1]]),
        np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),
    ]

@pytest.fixture
def additional_edge_locs():
    """
    Fixture que fornece uma lista de locais de borda adicionais de exemplo.
    """
    return [
        ([(15, 15), (25, 25)], (0, 255, 0)),
        ([(35, 35), (45, 45), (55, 55)], (0, 0, 255)),
    ]

@pytest.fixture
def additional_hex_colors():
    """
    Fixture que fornece uma lista de cores no formato hexadecimal adicionais de exemplo.
    """
    return ['#00FFFF', '#FFFF00']

@pytest.fixture
def additional_bgr_colors():
    """
    Fixture que fornece uma lista de cores no formato BGR adicionais de exemplo.
    """
    return [(255, 0, 255), (255, 255, 0)]

# Fixture para testar a função is_port_open

@pytest.fixture
def sample_ip():
    """
    Fixture que fornece um endereço IP de exemplo.
    """
    return "127.0.0.1"

@pytest.fixture
def sample_open_port():
    """
    Fixture que fornece um número de porta aberta de exemplo.
    """
    return 80

@pytest.fixture
def sample_closed_port():
    """
    Fixture que fornece um número de porta fechada de exemplo.
    """
    return 81

# Fixture para testar a função wait_for_service

def mock_healthcheck_server():
    """
    Função auxiliar que simula um servidor de healthcheck que fica disponível após algum tempo.
    """
    def start_mock_server():
        time.sleep(2)  # Simula o tempo de inicialização do servidor
        print("Healthcheck server is up and running!")

    server_thread = threading.Thread(target=start_mock_server)
    server_thread.start()

@pytest.fixture
def healthcheck_server():
    """
    Fixture que inicia um servidor de healthcheck mock e aguarda até que esteja disponível.
    """
    mock_healthcheck_server()  # Inicia o servidor mock de healthcheck
    time.sleep(1)  # Aguarda um tempo para o servidor iniciar