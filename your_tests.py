from calculator_adapter import run

def test_addition():
	result = run(["2", "+", "3"])
	asset "5" in result

def test_multiplication():
	result = run(["4", "*", "5"])
	asset "20" in result
