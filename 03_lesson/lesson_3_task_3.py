from Address import Address
from Mailing import Mailing


to_address = Address(348000, "г. Липецк", "ул. Свиридова", 14, 240)
from_address = Address(258000, "г. Воронеж", "ул. Пушкина", 5, 100)
track = "125896378"
cost = 12000

Mailing = Mailing(to_address, from_address, cost, track)

print(f"Отправление {Mailing.track} из {Mailing.from_address} в {Mailing.to_address}. Стоимость {Mailing.cost} рублей.")
