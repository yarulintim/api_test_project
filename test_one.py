import model_api
import common_to_all


def test_get_base():
    result = common_to_all.request('get', model_api.BASE_URL)
    print(result.status_code)
    return result