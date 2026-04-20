from calculator_adapter import run


def test_addition():
	result = run(["2", "+", "3"])
	assert "5" in result

def test_multiplication():
	result = run(["4", "*", "5"])
	assert "20" in result
