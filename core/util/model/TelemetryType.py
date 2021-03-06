from enum import Enum

class TelemetryType(Enum):
	TEMPERATURE = 'temperature'
	PRESSURE = 'pressure'
	HUMIDITY = 'humidity'
	LIGHT = 'light'
	GAS = 'gas'
	AIR_QUALITY = 'airQuality'
	UV_INDEX = 'uvIndex'
	NOISE = 'noise'
	CO2 = 'co2'
	RAIN = 'rain'
	SUM_RAIN_1 = 'sumRain1'
	SUM_RAIN_24 = 'sumRain24'
	WIND_STRENGTH = 'windStrength'
	WIND_ANGLE = 'windAngle'
	GUST_STRENGTH = 'gustStrength'
	GUST_ANGLE = 'gustAngle'
	DEWPOINT = 'dewPoint'
