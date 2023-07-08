from typing import Union
from abc import ABC, abstractclassmethod


class PaymentGateway(ABC):
    """Payment 인터페이스"""
    @abstractclassmethod
    def process_payment(self, card_num: str, amount: int):
        """추상화 process_payment 메서드"""
    @abstractclassmethod
    def _discount(self, discount_amount: int):
        """추상화 discount 메서드"""


class SRPPaymentGateway(PaymentGateway):
    def _discount():
        """강제로 작성해야하는 빈 메서드"""

    def process_payment(self, card_num: str, amount: int):
        print(
            f"SRP good 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class OCPPaymentGateway(PaymentGateway):
    def _discount():
        """강제로 작성해야하는 빈 메서드"""

    def process_payment(self, card_num: str, amount: int):
        print(
            f"OCP good 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class ISPPaymentGateway(PaymentGateway):
    def _discount(self, amount: int, discount_amount: int):
        return amount - discount_amount

    def process_payment(self, card_num: str, amount: int):
        amount = self._discount(amount, 500)
        print(
            f"ISP bad 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class CreditCard:
    def __init__(self, card_num: str):
        self.card_num = card_num


class CardService:
    def __init__(self, my_card: CreditCard, pay_gw: Union[SRPPaymentGateway, OCPPaymentGateway, ISPPaymentGateway]):
        self.my_card = my_card
        self.pay_gw = pay_gw
        if not isinstance(pay_gw, PaymentGateway):
            raise Exception("PaymentGateway가 아님")

    def pay_after(self, amount: int):
        card_num = self.my_card.card_num
        self.pay_gw.process_payment(card_num, amount)


isp_card = CreditCard('xxx-xxx-xxx-ISP')
isp_pay_gw = ISPPaymentGateway()
card_service = CardService(isp_card, isp_pay_gw).pay_after(1000)
