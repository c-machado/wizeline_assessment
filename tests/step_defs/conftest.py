import pytest


# print a message with the step in case of error
def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception
):
    print(
        f'Step failed: {step}', f'Scenario: {scenario}', f'Feature: {feature}'
    )

@pytest.fixture(params=['chrome'], scope='module', autouse=True)
def get_web_browser(request):
    return request.param


@pytest.fixture(params=['desktop'], scope='module', autouse=True)
def get_viewport(request):
    return request.param
