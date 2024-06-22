class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result: List[float] = []
        kelvin: float = celsius + 273.15
        fahrenheit: List[float] = celsius * 1.80 + 32
        result.append(kelvin)
        result.append(fahrenheit)
        return result
