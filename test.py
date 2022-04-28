import pytest
from config import Settings


def get_param():
    file_name = ['./Settings/setting.yml', './Settings/setting.env']
    rst = ['development', 'development']
    for i in range(2):
        yield file_name[i], rst[i]


def test_1(create_setting):
    print(create_setting.dict())
    assert 1


@pytest.mark.parametrize('file_name, rst', [('./Settings/setting.yml', 'development'),
                                            ('./Settings/setting.env', 'development')])
def test_2(file_name, rst):
    settings = Settings(_env_file=file_name, _env_file_encoding='utf-8')
    assert settings.ENV == rst


@pytest.mark.parametrize('file_name, rst', get_param())
def test_4(file_name, rst):
    settings = Settings(_env_file=file_name, _env_file_encoding='utf-8')
    assert settings.ENV == rst


def get_data_list_param():
    file_name = ['./Settings/setting.yml', './Settings/setting.env']
    rst = []
    yml_list = ['http://localhost:3002', 'http://localhost:3005', 'http://localhost:3006']
    env_list = ['http://localhost:3005', 'http://localhost:3006']
    rst.append(yml_list)
    rst.append(env_list)
    for i, j in zip(file_name, rst):
        yield i, j



class TestConfig:

    def test_err_yml_file_format(self):
        try:
            settings = Settings(_env_file='./Settings/err_file_format.yml', _env_file_encoding='utf-8')
        except Exception:
            assert 1
            return
        assert 0

    def test_err_yml_file_path(self):
        try:
            settings = Settings(_env_file='./Settings/test.yml', _env_file_encoding='utf-8')
        except FileNotFoundError:
            assert 1
            return
        assert 0

    @pytest.mark.parametrize('file_name', ['./Settings/err_data_format.yml', './Settings/err_data_format.env'])
    def test_err_data_format(self, file_name):
        try:
            settings = Settings(_env_file=file_name, _env_file_encoding='utf-8')
        except Exception:
            assert 1
            return
        assert 0

    @pytest.mark.parametrize('file_name, rst', get_data_list_param())
    def test_data_list(self, file_name, rst):
        settings = Settings(_env_file=file_name, _env_file_encoding='utf-8')
        assert settings.BACKEND_CORS_ORIGINS == rst

    @pytest.mark.parametrize('file_name', ['./Settings/setting.yml', './Settings/setting.env'])
    def test_data_replace(self, file_name):
        settings = Settings(_env_file=file_name, _env_file_encoding='utf-8')
        assert settings.ENV == 'development'
        assert settings.SERVER_HOST == 'http://localhost:3009'
        assert settings.DEBUG is True
        assert settings.LOG_TO_FILE is True
        assert settings.LOG_LEVEL == 'DEBUG'


if __name__ == '__main__':
    pytest.main(['-s', 'test.py'])
