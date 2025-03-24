import os


def get_mock_file_path() -> str:
    file_path = os.path.join(os.path.dirname(__file__), "test_files/Valores_del_Real_Madrid_2024.pdf")
    return file_path