import numpy as np
import sys
import os
import pytest
# Adicionando o diretório pai ao path para importar os módulos necessários
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Importando as funções a serem testadas
from functions import (
    obj_rect2coords, 
    compute_affine, 
    draw_edge_locs, 
    hex2bgr, 
    bgr2hex,
    is_port_open,
    wait_for_service
)
# Testes para as funções do módulo 'functions'

def test_obj_rect2coords(sample_obj_definition):
    """
    Testa se a função obj_rect2coords retorna as coordenadas corretas para um objeto retangular.
    """
    result = obj_rect2coords(sample_obj_definition)
    assert result == (10, 20, 30, 40, 0)

def test_compute_affine(sample_obj_definition, sample_dsize, sample_frame_affine_matrix):
    """
    Testa se a função compute_affine calcula corretamente uma transformação afim.
    """
    result = compute_affine(sample_obj_definition, sample_dsize, sample_frame_affine_matrix)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3)

def test_draw_edge_locs(sample_edge_locs, sample_color):
    """
    Testa se a função draw_edge_locs desenha corretamente as bordas na imagem.
    """
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    result = draw_edge_locs(frame, sample_edge_locs, sample_color)
    assert isinstance(result, np.ndarray)
    assert (result[sample_edge_locs[0]] == sample_color).all()
    assert (result[sample_edge_locs[1]] == sample_color).all()

def test_hex2bgr(sample_hex_color, sample_bgr_color):
    """
    Testa se a função hex2bgr converte corretamente uma cor hexadecimal para BGR.
    """
    result = hex2bgr(sample_hex_color)
    assert result == sample_bgr_color

def test_bgr2hex(sample_bgr_color, sample_hex_color):
    """
    Testa se a função bgr2hex converte corretamente uma cor BGR para hexadecimal.
    """
    result = bgr2hex(sample_bgr_color)
    assert result == sample_hex_color

def test_obj_rect2coords_additional(additional_obj_definitions):
    """
    Testa se a função obj_rect2coords lida corretamente com definições de objetos adicionais.
    """
    for definition in additional_obj_definitions:
        result = obj_rect2coords(definition)
        assert isinstance(result, tuple)

def test_compute_affine_additional(sample_dsize, additional_obj_definitions, additional_frame_affine_matrices):
    """
    Testa se a função compute_affine lida corretamente com definições de objetos e matrizes afins adicionais.
    """
    for definition, matrix in zip(additional_obj_definitions, additional_frame_affine_matrices):
        result = compute_affine(definition, sample_dsize, matrix)
        assert isinstance(result, np.ndarray)
        assert result.shape == (3, 3)

def test_draw_edge_locs_additional(additional_edge_locs):
    """
    Testa se a função draw_edge_locs desenha corretamente as bordas na imagem para locais de borda e cores adicionais.
    """
    for edge_locs, color in additional_edge_locs:
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        result = draw_edge_locs(frame, edge_locs, color)
        assert isinstance(result, np.ndarray)

def test_hex2bgr_additional(additional_hex_colors):
    """
    Testa se a função hex2bgr converte corretamente cores hexadecimais adicionais para BGR.
    """
    for hex_color in additional_hex_colors:
        result = hex2bgr(hex_color)
        expected_result = hex2bgr(hex_color)
        assert result == expected_result

def test_bgr2hex_additional(additional_bgr_colors):
    """
    Testa se a função bgr2hex converte corretamente cores BGR adicionais para hexadecimal.
    """
    for bgr_color in additional_bgr_colors:
        result = bgr2hex(bgr_color)
        expected_result = bgr2hex(bgr_color)
        assert result == expected_result

def test_is_port_open(sample_ip, sample_open_port, sample_closed_port):
    """
    Testa se a função is_port_open detecta corretamente se uma porta está aberta ou fechada.
    """
    # Testa se a porta aberta é detectada corretamente
    assert is_port_open(sample_ip, sample_open_port) == True
    # Testa se a porta fechada é detectada corretamente
    assert is_port_open(sample_ip, sample_closed_port)
    
def test_obj_rect2coords_invalid_definition():
    """
    Testa se a função obj_rect2coords lida corretamente com uma definição de objeto inválida.
    """
    invalid_definition = {'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0}
    with pytest.raises(KeyError):
        obj_rect2coords(invalid_definition)

def test_obj_rect2coords_invalid_scale():
    """
    Testa se a função obj_rect2coords lida corretamente com uma escala diferente de 1.
    """
    obj_definition = {'top': 10, 'left': 20, 'width': 30, 'height': 40, 'scaleX': 2, 'scaleY': 2, 'angle': 0}
    result = obj_rect2coords(obj_definition)
    assert result == (10, 20, 60, 80, 0)

def test_obj_rect2coords_invalid_angle():
    """
    Testa se a função obj_rect2coords lida corretamente com um ângulo diferente de 0.
    """
    obj_definition = {'top': 10, 'left': 20, 'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 45}
    result = obj_rect2coords(obj_definition)
    assert result == (10, 20, 30, 40, 45)

# Testes para a função compute_affine

def test_compute_affine_invalid_definition():
    """
    Testa se a função compute_affine lida corretamente com uma definição de objeto inválida.
    """
    invalid_definition = {'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0}
    dsize = (100, 100)
    frame_affine_matrix = np.identity(3)
    with pytest.raises(KeyError):
        compute_affine(invalid_definition, dsize, frame_affine_matrix)

def test_compute_affine_invalid_frame_matrix():
    """
    Testa se a função compute_affine lida corretamente com uma matriz de transformação de quadro inválida.
    """
    obj_definition = {'top': 10, 'left': 20, 'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0}
    dsize = (100, 100)
    invalid_frame_affine_matrix = np.zeros((3, 2))
    with pytest.raises(ValueError):
        compute_affine(obj_definition, dsize, invalid_frame_affine_matrix)
