from typing import Union


class SRPPaymentGateway:
    def srp_process_payment(self, card_num: str, amount: int):
        print(f"SRP good 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class OCPPaymentGateway:
    def ocp_process_payment(self, card_num: str, amount: int):
        print(f"OCP bad 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class CreditCard:
    def __init__(self, card_num: str):
        self.card_num = card_num


class CardService:
    def __init__(self, my_card: CreditCard, pay_gw: Union[SRPPaymentGateway, OCPPaymentGateway]):
        self.my_card = my_card
        self.pay_gw = pay_gw
        if not isinstance(pay_gw, OCPPaymentGateway):
            raise Exception("OCPPaymentGateway가 아님")

    def pay_after(self, amount: int):
        card_num = self.my_card.card_num
        self.pay_gw.ocp_process_payment(card_num, amount)


ocp_card = CreditCard('xxx-xxx-xxx-OCP')
ocp_pay_gw = OCPPaymentGateway()
card_service = CardService(ocp_card, ocp_pay_gw).pay_after(1000)

# SRP로 다시 바꿀 경우 에러가 발생됨
srp_card = CreditCard('xxx-xxx-xxx-SRP')
srp_pay_gw = SRPPaymentGateway()
card_service2 = CardService(srp_card, srp_pay_gw).pay_after(1000)
