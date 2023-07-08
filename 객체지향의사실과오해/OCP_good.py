from typing import Union
from abc import ABC, abstractclassmethod


class PaymentGateway(ABC):
    """Payment 인터페이스"""
    @abstractclassmethod
    def process_payment(self, card_num: str, amount: int):
        """추상화 Payment Gateway 메서드"""


class SRPPaymentGateway(PaymentGateway):
    def process_payment(self, card_num: str, amount: int):
        print(
            f"SRP good 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class OCPPaymentGateway(PaymentGateway):
    def process_payment(self, card_num: str, amount: int):
        print(
            f"OCP good 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class CreditCard:
    def __init__(self, card_num: str):
        self.card_num = card_num


class CardService:
    def __init__(self, my_card: CreditCard, pay_gw: Union[SRPPaymentGateway, OCPPaymentGateway]):
        self.my_card = my_card
        self.pay_gw = pay_gw
        if not isinstance(pay_gw, PaymentGateway):
            raise Exception("PaymentGateway가 아님")

    def pay_after(self, amount: int):
        card_num = self.my_card.card_num
        self.pay_gw.process_payment(card_num, amount)


ocp_card = CreditCard('xxx-xxx-xxx-OCP')
ocp_pay_gw = OCPPaymentGateway()
card_service = CardService(ocp_card, ocp_pay_gw).pay_after(1000)

# 이젠 SRP로 해도 에러가 발생하지 않음
srp_card = CreditCard('xxx-xxx-xxx-SRP')
srp_pay_gw = SRPPaymentGateway()
card_service2 = CardService(srp_card, srp_pay_gw).pay_after(1000)
